"""
Talkweb Examples
gate.py
A facade to load responders for each http request
This example uses wsgitalkback to manage session and cookie
"""
from wsgitalkback import *

def application(environ,start_response):
	""" default handler for http request """
	status = '200 OK'
	output = 'Cannot find requested page '

	usession=None
	sk = sessionkeepers.keeper(environ)

	cookies=html_cookies.fromrequest(environ)
	sessioncookie=session.identify(cookies,"TALKWEB_EXAMPLE")

	if sessioncookie:
		usession = sk.getfrom(sessioncookie)


	response_headers=[]
	if not usession:
		usession=sk.new("TALKWEB_EXAMPLE")
		#scookie.set all attributes
		scookie = usession.tocookie()
		scookie.sethttponly()
		#scookie.setsecure()
		response_headers=html_cookies.toinject([scookie])

	responder=responders.uriresponder()
	pageresponder=responder.respondfor(environ,usession,cookies)
		
	if pageresponder:
		status,xresponse_headers,output=pageresponder.respond()
		if not status:
			status = '200 OK'
		if "Content-type" not in xresponse_headers:
			response_headers.append(("Content-type","text/html;charset=utf-8;"))
		if "Content-Length" not in xresponse_headers:
			response_headers.append(("Content-Length",str(len(output))))
		
		for aheader in xresponse_headers:
			response_headers.append(aheader)
		
	start_response(status,response_headers)
	return output
