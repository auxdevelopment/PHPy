"""
Web server for the framework

Usage:

  start   -   starts server
  stop    -   stops server
  restart -   restarts server if its already running

"""


import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
from config import Config
sys.path.insert(0, "parser/")
import parser


class RequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    print("Client: " + str(self.client_address))
    try:
      self.send_response(200) # http-code: 200 -> OK
      self.send_header("Content-type", self.getMimeType())
      self.end_headers()
      if(self.getMimeType().find("text") != -1):
        contentBytes = self.getContent()
        # pass the path of the file to the parser so he can chdir to it
        content = parser.parse(contentBytes.decode("utf-8"), self.getPath()) 
        

        self.wfile.write(bytes(content, "utf-8"))
  
      else:
        self.wfile.write(self.getContent())

    except FileNotFoundError as fnfe:
      print("File not found: " + str(fnfe))
    except IOError:
      self.send_error(404, "File not found: " + self.path)

  def do_POST(self):

    length = int(self.headers["Content-Length"])
    print("Data: " + str(self.rfile.read(length), "utf-8"))
    #response = bytes("self", "utf-8") #create response
    #self.send_response(200) #create header
    #self.send_header("Content-Length", str(len(response)))
    #self.end_headers()
    #self.wfile.write(response) #send response


  def getContent(self):
    indexFile = open(os.getcwd() + "/html" + self.path, "br")
    content = indexFile.read()
    indexFile.close()
    return content


  def getMimeType(self):
    typesDict = {
      "image":["gif", "jpg", "png"],
      "text":["html", "txt", "css", "c", "cpp", "java"],
      "application":["js"]
    }

    for key in typesDict:
      for extension in typesDict[key]:
        if self.path.endswith("." + extension):
           return key + "/" + extension
    return "text/html" # to avoid NoneType errors


  def getPath(self):
    return os.path.dirname(os.getcwd() + "/html/" + self.path)

########## End of class section ############


def startServer():
    server = HTTPServer(("localhost", 80), RequestHandler)
    print(time.asctime(), "Server started on port 80")
    
    try:
      server.serve_forever()
    
    except KeyboardInterrupt:
      print("Server stopped...")


if __name__ == "__main__":
  if len(sys.argv) == 2:
    if sys.argv[1] == "start":
      startServer()
    if sys.argv[1] == "stop":
      pass # stopServer()

    if sys.argv[1] == "restart":
      pass # restart() = start();stop()
  else:
    print("ERROR: no argument added")

