"""
Web server for the framework

Usage:

  start   -   starts server
  stop    -   stops server
  restart -   restarts server if its already running

"""

#TODO: dont ignore the config file...

import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os
from config import Config
sys.path.insert(0, "parser/")
import parser


class RequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    print("GET-Request from " + str(self.client_address))
    
    try:

      self.send_response(200) # http-code: 200 -> OK
      self.send_header("Content-type", self.getMimeType())
      self.end_headers()

      if((self.getMimeType() != None) and (self.getMimeType().find("text") != -1)): # text file
        contentBytes = self.getContent()

        get = ""

       # if get != "":
        #  content = parser.parse(contentBytes.decode("utf-8"), self.getPath(), GET=get)
        #else:
        content = parser.parse(contentBytes.decode("utf-8"), self.getPath())
          
        self.wfile.write(bytes(content, "utf-8"))
  
      else: # binary file, for example: jpg, png, pdf etc..
        self.wfile.write(self.getContent())

    except FileNotFoundError as fnfe:
      print("File not found: " + str(fnfe))

    except IOError:
      self.send_error(404, "File not found: " + self.path)


  def do_POST(self):

    length = int(self.headers["Content-Length"])
    print("POST-Data: " + str(self.rfile.read(length), "utf-8"))
    response = bytes("self", "utf-8") #create response
    self.send_response(200) #create header
    self.send_header("Content-Length", str(len(response)))
    self.end_headers()
    self.wfile.write(response) #send response


  def getContent(self):
    modifiedPath = self.path.split("?")[0] # www.example.com/test.html?value=0 ---> www.example.com/test.html
    indexFile = open(os.getcwd() + "/html" + modifiedPath, "br")
    content = indexFile.read()
    indexFile.close()
    return content

  #TODO: download list of all mime types and create the dictionary at startup
  def getMimeType(self):
    typesDict = {
      "image":["gif", "jpg", "png"],
      "text":["html", "txt", "css", "c", "cpp", "java"],
      "application":["js"],
      "octet-stream":["pdf"]
    }

    for key in typesDict:
      for extension in typesDict[key]:
        if self.path.endswith("." + extension):
           return key + "/" + extension
    return "text/html" # to avoid NoneType errors


  def getPath(self):
    return os.path.dirname(os.getcwd() + "/html/" + self.path)

  def getGetValues(): # returns array with values
    pass
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
  else:
    print("ERROR: no argument added")

