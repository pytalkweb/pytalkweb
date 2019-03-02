"""
myresponder
filename is used to call from url
all responders are myresponders if you did not notice
Copyright (c) Madhukumar Seshadri
"""
from wsgitalkback import *
from talkweb import *

class myresponder(uiresponder):
	""" 	
		self.usession
		self.cookies
		self.headers_that_came_in
		self.headers_that_need_to_go_out
		self.incoming_data
	"""

	def respond(self):
		""" your response please """
		status = '200 OK'
		response_headers=[]

		#application name
		an = appname(self.environ)
		#wsgi alias for application configured in apache conf
		wan = wsgialias(self.environ)
		#application base directory
		abd = appbasedir(self.environ)

		#print to apache log
		#print 'an',an,'wan',wan,'abd',abd

		fn = abd + os.sep + 'html' + os.sep + "helloworld.html"
		#come to object (cells) from html file
		page=h2oo(fn)
		#find the hello world container cell within the page
		hwc=page.findcellbyid("helloworldcontainer")
		#add hello world cell from string by adding 's' to h2oo (html to object)
		hwc.addcell(h2oo("<div>Hello World</div>",'s'))

		#return these to gate.py
		return (status,response_headers,page.html())

