talkweb 
=======

A small server side framewok written in python to build web applications rapidly. It has three modules,
1) talksql - A wrapper to mysql-connector  
2) wsgitalkback - A responder framework
3) talkweb - A html elements (calling it cell) to object and object to html framework on server side. This allows you to import html and find elements to manipulate them in your python code. You can simply write a responder to every http request and build html and python objects. Instead of templating engine, you can be in python object and keep importing, injecting and manipulating html. Please see examples. 

Works with python 2.X. Look for python 3.X at pytalkweb/pytalkweb3.

Download the zip file and deploy by install modules separately, 
1) Run python setup.py install from talksql directory 
2) Run python setup.py install from wsgitalkback directory
3) Run python setup.py install from talkweb directory

What's talksql?

A wrapper for mysqlconnector. It has global functions for most redundantly used functions with mysql connector.

As an example, 
con = sockconnect(db=dbname);
rs,c=xecrs(con,sql)

returns result-set in [[col1,col2.. ]] and cursor for any residual use in state as c.

It also has functions like sqlofa making easier to put together insert statements. Check out sqli.py inside talksql directory for more. It is advised that sockconnect or ipconnect functions to be moved to application code and see them as only skeleton code.

What's wsgitalkback?

A responder framework to work with any wsgi (web server gateway interface). It uses cookie, query string, posted form data extractions in accordance to RFC 2616-hypertext transfer protocol and RFC 2965 that defines cookie protocols. It also implements a responder framework to respond to each http request and a session keeper to manage server end user session. A typical application uses this framework implements responders for each http requests. A sample responder is provided as simpleresponder.py in the examples. A facade gate.py, which acts as gateway to responders is also provided.


What's talkweb?

As an example, in your python interpreter, try this,
from talkweb import *
c = cell(tag="div");
c.data="Hello world";
c.html();

Write your html in string and use
h2o('html string','s') to bring to object structure (cells) or 
h2o('html file path') to bring html to object structure (cells) for converting html files to objects.

You can use <anycell>.addcell to add the cells to that cell. To get the existing cell use
<anycell>.findcellbyid("id") where id is attribute id of the cell.

You can use html snippets in code and convert them to cells and work with them like you work with document object model on the client side with javascript, here with python. Most frameworks work the other way allow code substituitions inside html. I find it easy to code or logic first before writing html while writing server code, hence talkweb. 

Using talkweb with apache, mysql and mod_wsgi,
1.  Install apache or any other webserver
2.  Install mysql server or any other relational database
3.  Install mysqlconnector setup.py - python connector to mysql database or it's equivalent to your database
4.  Install mod_wsgi setup.py - apache plugin for WSGI implementation

Now to the talkweb setup which was described above as deploying talkweb, run the setup.py in each of the folders, talkweb, talksql and wsgitalkback.
 
Deploying examples

Use deploy script provided in examples to deploy your talkweb app. You have choose a path for your applications. I'm using /usr/local/app/ex for examples app responders and htmls. Choose your path and change that in deploy script accordingly.

Configure gate.py as WSGIScriptAlias for the app examples in apache httpd.conf,

WSGIScriptAlias /examples /usr/local/app/ex/gate.py
<Directory "/usr/local/app/ex">
Order allow,deny
Allow from all
</Directory>

 You would simply call the responder via the url or post for each request, an example of this
http://localhost/examples?r=simpleresponder

The cell framework can be expanded like jquery 
1) to incorporate css pattern matching capabilities to get elements 
2) chaining
