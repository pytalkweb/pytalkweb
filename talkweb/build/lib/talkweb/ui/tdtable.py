""" table (html table) 
purpose - make an html table
version -- I don't keep it till I get a first cut unknown
author -- none other than Madhukumar Seshadri
copyright -- All rights reserved to Madhukumar Seshadri 
license -- see copyright
"""
from talkweb import *

class tdtable(cell):
	""" atable """
	def __init__(self,tableid=""):
		""" create the table """
		cell.__init__(self,tag="table")
		self.headercontainer=self.addcell(cell(tag="tr"))
		self.headercontainer.addattrib("id","headercontainer")
		self.datacontainer=self.addcell(cell(tag="tbody"))
		self.datacontainer.addattrib("id","datacontainer")
		self.statusrow=""
		self.rowcount=0;
		self.colcount=0;

	def addcellat(self,x,y,incomingcell):
		""" add the incoming cell at row,col"""
		#incomingcell.css.place.display="table-cell"
		incomingcell.settag("td")
		if x < self.rowcount:
			#print "row:",x,"is within bounds"
			if y < self.colcount:
				#print "col:",y,"is within bounds"
				self.datacontainer.listofcells[x].listofcells[y]=incomingcell
				incomingcell.parent=self.datacontainer.listofcells[x]
				return incomingcell
			else:
				#print "y:",y,"is not within bounds"
				for i in range(y+1)[self.colcount:y+1]:
					tdcell = self.datacontainer.listofcells[x].addcell(cell(tag="td"))
					tdcell.addattrib("id","col"+str(i))
					
				#header
				headercolcount = len(self.headercontainer)
				if headercolcount < y:
					for i in range(y+1)[headercolcount:y+1]:
						headercell=self.headercontainer.addcell(cell(tag="th"))
						headercell.addattrib("id","col"+str(i))
						#headercell.css.place.display="table-cell"
				#header end
				self.colcount=y+1
		else:
			#print "given x",x,"is not within bounds",self.rowcount,
			expandexistingrows=0
			if y < self.colcount:
				#print "given y",y,"is within bounds",self.colcount
				colbounds=self.colcount
			else:
				#print "given y",y,"is not within bounds",self.colcount
				colbounds=y+1;
				expandexistingrows=1
			
			existingrows=range(self.rowcount)
			newrows=range(x+1)[self.rowcount:x+1]
			#print "newrows",newrows,"existingrows",existingrows,"colbounds",colbounds
			for i in newrows:
				rowcontainer=self.datacontainer.addcell(cell(tag="tr"))
				rowcontainer.addattrib("id","row"+str(i),)
				#rowcontainer.css.place.display="table-row"
				for j in range(colbounds):
					acell=rowcontainer.addcell(cell(tag="td"))
					acell.addattrib("id","col"+str(j))
					#acell.css.place.display="table-cell"

			self.rowcount += len(newrows)

			newcols=range(colbounds)[self.colcount:colbounds+1]

			#headerrow
			headercolcount=len(self.headercontainer)
			if headercolcount < y:
				newheadercols=range(colbounds)[headercolcount:colbounds+1]
				for j in newheadercols:
					headercell=self.headercontainer.addcell(cell(tag="th"))
					headercell.addattrib("id","col"+str(j))
					#headercell.css.place.display="table-cell"
			#headrow end

			if expandexistingrows:
				for i in existingrows:
					rowcontainer=self.datacontainer.listofcells[i]
					for j in newcols:
						acell=rowcontainer.addcell(cell(tag="td"))
						acell.addattrib("id","col"+str(j))
						#acell.css.place.display="table-cell"
						#headercell=self.headercontainer.addcell(cell(cellid="col"+str(j)))
						#headercell.css.place.display="table-cell"

			self.colcount += len(newcols)

		self.datacontainer.listofcells[x].listofcells[y]=incomingcell
		incomingcell.parent = self.datacontainer.listofcells[x]
		return incomingcell

	def cellat(self,x,y):
			""" returns the cell at """
			return self.datacontainer.listofcells[x].listofcells[y]

	def setlegendcellat(self,cno,headercell):
			""" set the legend cell as headercell """
			if cno < len(self.headercontainer.listofcells):
				self.headercontainer.listofcells[cno]=headercell

	def html(self):
		return cell.html(self)
	
if __name__ == "__main__":
	#cond #1 atable = table(0,1)
	#cond #1 atable = table(0,1)
	atable = tdtable()
	atable.setlayout("fixed")
	atable.setcolumnsize(0,"130px")
	print atable.html()
	#print atable.html()
