""" 
session.py
Author - Madhukumar Seshadri
keepers, keeper and payload - for session
	keepers give me a keeper
	keeper <crud> the session
"""
import uuid
import os
from cookie import *
from app import *
from talksql import *
from cPickle import *
from path import *

_session_store_suffix=".store"

idgen=uuid.uuid1

class session:
	""" payload """
	@classmethod
	def identify(cls,listofcookies,sci):
		for acookie in listofcookies:
			if acookie.name==sci:
				return acookie

	def __init__(self,sci,value={}):
		""" you can create this or you can get this from cookie """
		self.sci=sci
		self.id=str(idgen())
		self.store={}
		#self.new=1

	def __str__(self):
		""" string representation """
		return self.id + ":" + str(self.store)

	def tocookie(self):
		""" make cookie of me """
		return cookie(self.sci,self.id)

	def persist(self,environ):
		sessionkeepers.keeper(environ).put(self)

	def invalidate(self,environ):
		self.store={}
		sessionkeepers.keeper(environ).pop(self)

class sqlsessionkeeper:
	""" 	ask sessionkeepers akeeper for me and not directly
		  I store and retrieve sessions
	"""
	def __init__(self,environ):
		#self.request=req
		self.conn=sockconnect()
		use(self.conn,"session")
		self.environ=environ

	def getfrom(self,sessioncookie):
		""" input is sessioncookie identified by session object """
		return self.get(sessioncookie.value)

	def get(self,sessionid):
		""" input is sessionid """
		rs,c=xecrs(self.conn,'select obj from session where sessionid='+'"' + sessionid +'"')
		obj=None
		if len(rs) > 0:
			if len(rs[0]) > 0:
				obj=loads(rs[0][0])
		return obj

	def put(self,s):
		""" where s is session object possibly created using session cookie"""
		if self.get(s.id):
			xec(self.conn,"update session set obj = " + '"' + dumps(s) + \
				'" where sessionid = "' + s.id + '"')
		else:
			xec(self.conn,'insert into session (sessionid, obj) values (' +\
			 '"' + s.id + '","' + dumps(s) + '")')

	def pop(self,s):
		""" where s is session object """
		# _@todo deleteincache
		xec(self.conn,'delete from session where sessionid = ' + '"' + s.id + '"')

	def new(self,sci):
		""" returns a new session """
		asession = session(sci)
		xec(self.conn,'insert into session (sessionid, obj) values (' +\
			 '"' + asession.id + '","' + dumps(asession) + '")')
		return asession



class fskeeper:
	""" 	ask sessionkeepers akeeper for me and not directly
		  I store and retrieve sessions	"""
	def __init__(self,environ):
		#self.request=req
		self.environ=environ

	def getfile(self,sessionid):
		basedir = appbasedir(self.environ)
		sessionsroot = basedir + os.sep + "sessions"
		output=filesusingfilter(sessionsroot,sessionid)
		if len(output) < 1:
			print "wsgitalkback:sessionid",sessionid,"did not qualify"
			#@todo cookie need to be told wipe off
			return ""
		return sessionsroot + os.sep + output[0][0]

	def getfrom(self,sessioncookie):
		""" input is sessioncookie identified by session object """
		return self.get(sessioncookie.value)

	def get(self,sessionid):
		""" input is sessionid """
		obj=None
		fn=self.getfile(sessionid)
		if not fn:
				return None
		try:
			f=open(fn,"r")
			s=f.read()
		except IOError, e:
			print "fskeeper",e
		if s:
			obj=loads(s)
		f.close()
		return obj

	def put(self,s):
		""" where s is session object possibly created using session cookie"""
		fn=self.getfile(s.id)
		if not fn:
			print "wsgitalkback:grave error session file cannot be found", sessionid
		f=open(fn,"w")
		x=dumps(s)
		f.write(x)
		f.close()

	def pop(self,s):
		""" where s is session object """
		# _@todo deleteincache
		fn=self.getfile(s.id)
		if not fn:
			print "wsgitalkback:grave error session file cannot be found", sessionid
		os.remove(fn)

	def new(self,sci):
		""" returns a new session """
		basedir = appbasedir(self.environ)
		sessionsroot = basedir + os.sep + "sessions"
		asession = session(sci)

		#create sessions directory if not exists
		f = open(sessionsroot + os.sep + asession.id,"w")
		self.put(asession)
		f.close()

		return asession

class sessionkeepers:
	""" inorder to have many, there need to be one, hence I was forged """
	akeeper=sqlsessionkeeper

	@classmethod
	def keeper(cls,environ):
		return cls.akeeper(environ)

	@classmethod
	def setkeeper(cls,keeperclassobj,module):
		# _@todo dyn import the module
		cls.akeeper=keeperclassobj


""" Template do not erase inherit .. 
class sessionkeeper:
	# 	ask sessionkeepers akeeper for me and not directly
	#	  I store and retrieve sessions
	def __init__(self,environ):
		#self.request=req
		self.filepath=appbasedir(environ) + "/" + appname(environ) + _session_store_suffix
		self.mystore=filestore
		#self.replicator=replication service to replicate values to others
		#self.mycache = "__not_available__"

	def getfrom(self,sessioncookie):
		#input is sessioncookie identified by session object
		return self.mystore.get(sessioncookie.value,self.filepath)

	def get(self,sessionid):
		# input is sessionid
		return self.mystore.get(sessionid,self.filepath)

	def put(self,s):
		# where s is session object possibly created using session cookie
		# _@todo retrievefromcache and updatecache
		#self.mystore.pop(s.key,self.store)
		self.mystore.put(s,s.id,self.filepath)

	def pop(self,s):
		#where s is session object
		# _@todo deleteincache
		return self.mystore.pop(s.id,self.filepath)

	def new(self,xsession=None):
		#returns a new session
		if xsession is None:
			asession = session()
		else:
			asession=xsession
		self.put(asession)
		return asession
"""