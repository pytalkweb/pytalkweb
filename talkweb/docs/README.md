talkweb 
=======

Deploying talkweb 

Run python setup.py in talkweb directory 
Run python setup.py in wsgitalkback directory
Run python setup.py in talksql directory


What's talkweb?

Talkweb is a way of building web pages in python using the document object model like object models on the server side.  

As an example, in your python interpreter,
from talkweb import *
c = cell(tag="div")
c.data="Hello world"
c.html()

Write your html in string and use
h2o('html string','s') to bring to object structure (cells) or 
h2o('html file path') to bring html to object structure (cells) for converting html files to objects.

You can use anycell.addcell to add the cells to that cell. To get the existing cell use
anycell.findcellbyid("id") where id is attribute id of the cell.

You can use html snippets in code and convert them to cells and work with them like you work with document object model on the client side with javascript, here with python. Most frameworks work the other way allow code substituitions inside html. I find it easy to code first or write html while writing server logic, hence talkweb. 

Cell framework can be expanded like jquery and incorporate css pattern matching capabilities to manipulate cells (elements).

What's wsgitalkback?

A responder framework to work with any wsgi (web server gateway interface). It uses cookie, query string, posted form data extractions in accordance to RFC 2616-hypertext transfer protocol and RFC 2965 that defines cookie protocols. It also implements a responder framework to respond to each http request and session keeper to manage server end user session. A typical application uses the framework implements responders for each http requests. A sample responder is provided as sampleresponder.py. A facade gate.py shows uses of wsgitalkback framework acts as gateway to responders.

What's talksql?

A wrapper around mysqlconnector or it's equivalent to any database. It has global functions for most redundant used functions.

con = sockconnect(db=dbname)
rs,c=xecrs(con,sql)

returns result-set in [[col1,col2.. ]] and cursor for any residual use in state as c.

It also has functions like sqlofa making easier to put together insert statements. Check out sqli.py inside talksql directory for more. It is advised that sockconnect or ipconnect functions to be moved to application code and see them as skeleton code.

Using talkweb with apache, mysql and mod_wsgi,
1.  Install apache or any other webserver
2.  Install mysql server or any other relational database
3.  Install mysqlconnector setup.py - python connector to mysql database or it's equivalent to your database
4.  Install mod_wsgi setup.py - apache plugin for WSGI implementation

After this, configure gate.py as WSGIScriptAlias for the app,
I have attached gate.py a facade to work with wsgitalkback and sampleresponder, getresponder, postresponder

If you are using gate.py, you would simply call the responder via the url or post for each request.

4. Installed talkweb python module
5. Installed talksql python module
6. Installed wsgitalkback python module
7. Change apache's httpd.conf 
    WSGIScriptAlias /appname /usr/local/app/dkn/gate.py
    <Directory "/usr/local/app/dkn">
    Order allow,deny
    Allow from all
    </Directory>
8. Image folders need to htdocs and permission have to given for admin app
    1. /usr/local/apache2/htdocs/appname/img permission for apache user (daemon)








