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
  template = open("parser/template.py", "r")
  content = template.read()
  template.close()
  return content


def replacePythonTags(html, output):
  start = html.index("<?python")
  end = html.index("?>") + len("?>")
  return html.replace(html[start:end], output)

 # main function of the parser, server will only call this method
def parse(htmlContent):
  #check if there are any <?python tags
  if not containsPythonCode(htmlContent):
    return htmlContent 
  
  pythonCode = getPythonCode(htmlContent)
  templateContent = loadTemplate()
  out = templateContent.replace("INSERT", pythonCode)

  #replace OUTPUT_FILE
  out = out.replace("OUTPUT_FILE", "/tmp/out")
  
  os.system("python3 -c '" + out + "'") # runs script

  outputFile = open("/tmp/out", "r")
  output = outputFile.read()
  outputFile.close()

  return replacePythonTags(htmlContent, output)
