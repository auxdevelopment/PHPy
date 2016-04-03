# PHPy
Webserver and python parser for using python instead of php.


#What works
 - Hosting HTML webpages with multimedia content
 - Using python for server-side scripting
 - multiple python tags in one file
 
#What doesn't work (yet)
 - using POST and GET values from http session

#Usage
 - Starting server: `$ python3 server.py start`

 - To use python inside an html document you have to write something like this:

 ```html
 <html>
  <body>
 <?python
 print("Put your python code here!")
 ?>
  </body>
 </html>
 ```
 - The html files rest under the `server/html` directory
 - Notice that currently the python tags have to be at the left side of the document! This will probably change in future...
