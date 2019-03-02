#FIX-ME - kvc does not guarantee order inwhich string will be converted for dictionary values
# if you change the onwhat dict keys - create table onwhat expansion need to be altered otherwise
# .......
# expiry for options are not stored as datetime but as a weird string

import re
import time
#from nomads import *
from sqli import *

#should return default db name holding trans/pos
def ddb():
	return db

def createtables():
	conn = sockconnect("trans")
	s1 = "drop table if exists trans"
	s2 = "drop table if exists positions"
	s3 = "create table trans (id float, broker text, time datetime, tcode char(2), ttype text, tsubtype text, odir text, strike float, ul text, syb text, dl float, sect text,exp text, p float,q float,c float, f float, amt float,original text,osyb text)"
	s4 = "create table positions (ont datetime, syb text, qty float, mps float, cps float, f1 text, f2 text)"
	xec(conn,s1)
	xec(conn,s2)
	xec(conn,s3)
	xec(conn,s4)

def test_trandb():
	return 1

def pefq(x,q):
	y="" 
	for i in range(len(x)):
		if x[i] != q:	
			y=y+x[i]
		else:
			y=y+"\\"
			y=y+x[i]
	return str(y) 

def cat(x):
	r=""
	for i in range(len(x)):
		if re.findall(",",x[i]):
			#r = r + '\\"' + x[i] + '\\"' + ","
			#r = r + '\'' + x[i] + '\'' + ","
			r = r + x[i] + ","
		else:
			r = r + x[i] + ","
	r = r[0:len(r)-1]	
	return r

def getnextid(t):
	dbc = sockconnect("trans")
	c = dbc.cursor()
	c.execute("select max(id) from " + t)
	for i in c:
		x = i[0]
		if x is None:
			return 0.0
		else:
			return x + 1.0
	dbc.close()

def insert_tran(x,bank,bmap):
	nid = str(getnextid("trans"))
	sql = "insert into tran values ( " +\
	nid + "," + \
	'"' + bank + '",' + \
	"'" + time.strftime("%Y-%m-%d %H:%M:%S",bmap.whent(x)) + "'" + "," + \
	kvc(bmap.what(x)) + "," + \
	kvc(bmap.onwhat(x)) + "," + \
	str(bmap.pps(x)) + "," + \
	str(bmap.qty(x)) + "," + \
	str(bmap.com(x)) + "," + \
	str(bmap.fee(x)) + "," + \
	str(bmap.amt(x)) + "," + \
	'"' + cat(x) +  '"' + "," + \
	'"' + bmap.syb(x) + '"' + "," +\
	"'" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) + "'" + ")" 
	c = dbc.cursor()
	print sql
	c.execute(sql)
	dbc.commit()
	c.close()

def export_orig(forbank,fn):
	f=open(fn,"w")
	r=xecr(ddb(),"select original from trans where broker=" + "'" + forbank + "' order by time desc")
	for i in r.keys():
		f.write(r[i][0])
		f.write("\n")
	f.close()

def load_tran(forbank):
	tr={}
	ic=0
	sql = "select * from tran where broker = " + "'" + forbank + "' order by time desc"
	dbc = sockconnect("trans")
	c = dbc.cursor()
	#print "executinig sql ", sql
	c.execute(sql)
	for i in c:
		tr[ic]=[]
		for j in range(len(i)):
			tr[ic].append(i[j])
		ic += 1
	c.close()
	return tr
	
def insert_pos(x):
	sql = kvc (x)
	dbc = sockconnect("trans")
	c = dbc.cursor()
	c.execute(sql)
	dbc.commit()
	c.close()
