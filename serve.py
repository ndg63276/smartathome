#!/usr/bin/env python

import sys
if sys.version_info[0] == 3: # python3

	from http.server import HTTPServer, CGIHTTPRequestHandler
else: # python2
	from BaseHTTPServer import HTTPServer
	from CGIHTTPServer import CGIHTTPRequestHandler
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = HTTPServer
handler = CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/cgi-bin"]
 
httpd = server(server_address, handler)
httpd.serve_forever()
