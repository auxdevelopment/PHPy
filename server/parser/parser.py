"""
Parser module for Python webframework


examples:
<html>
  <?python
    print("Hello World")
  ?>
</html>

-> will print "Hello world" to the html document

template-file = template.py

template-file insert points:
  - OUTPUT_FILE = the output file used instead of sys.stdout
  - INSERT = the actual code
  - GET = get dictionary
  - POST = post dictionary
"""
import re
import os

#checks if the html file contains python code
def containsPythonCode(htmlContent):
  if((htmlContent.find("<?python") != -1) and (htmlContent.find("?>") != -1)):
      return True
  return False


# filters python code from html code
def getPythonCode(htmlContent):
  try:
    start = htmlContent.index("<?python") + len("<?python")
    end = htmlContent.index( "?>", start)
    return htmlContent[start:end]
  except ValueError:
    return ""


#reads the content of the template.py file
def loadTemplate():
  with open("parser/template.py", "r") as template:
    content = template.read()
  return content


def create_GET_Dict(GET): # creates a dictionary out of a passed string
  pass 
  


def replacePythonTags(html, output):
  start = html.index("<?python")
  end = html.index("?>") + len("?>")
  return html.replace(html[start:end], output)

 # main function of the parser, server will only call this method
def parse(htmlContent, path, GET="", POST=""):
  #check if there are any <?python tags
  if not containsPythonCode(htmlContent):
    return htmlContent 
  
  pythonCode = getPythonCode(htmlContent)
  templateContent = loadTemplate()
  out = templateContent.replace("INSERT", pythonCode)


  ####GET Section########
  if GET != "":
    GET_Dict = create_GET_Dict(GET)
    out = out.replace("GET", "GET = " + str(GET_Dict))
  else:
    out = out.replace("GET", "") # remove get from template
  ####End GET Section###

  ####POST Section#####
    if POST != "":
      POST_Dict = create_POST_Dict(POST)
      out = out.replace("POST", "POST = " + str(POST_Dict))
    else:
      out = out.replace("POST", "") # remove post from template

  ####End POST section##

  output = os.popen("cd " + path + " && python3 -c '" + out + "'").read() # runs script
   
  result = replacePythonTags(htmlContent, output)
  if containsPythonCode(result):
    return parse(result, path)
  return result
