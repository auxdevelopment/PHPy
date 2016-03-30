# PHPy
Webserver and python parser for using python instead of php.


#What works
 - Hosting HTML webpages with multimedia content
 - Using python for server-side scripting
 
#What doesn't work (yet)
 - using POST and GET values from http session
 - multiple python calls in one file

#Usage
 - Starting server: `$ python3 server.py start`

 - To use python inside an html document you have to write something like this:

 ```html
 <html>
 <?python
 print("Put your python code here!")
 ?>
 </html>
 ```
 - The html files rest under the `server/html` directory
