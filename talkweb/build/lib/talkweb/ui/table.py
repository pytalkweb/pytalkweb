""" table (html table) 
purpose - make an html table
version -- I don't keep it till I get a first cut
author -- none other than Madhukumar Seshadri
copyright -- All rights reserved to Madhukumar Seshadri 
license -- see copyright
"""
from talkweb import *

class table(cell):
	""" atable """
	def __init__(self):
		""" create the table """
		cell.__init__(self)
		self.tdata=[]
		self.addattrib("style:{display:table;}")
		self.pcellcontainer=self.addcell(cell())
		self.pcellcontainer.addattrib("id","pcellcontainer")
		self.headercontainer=self.addcell(cell())
		self.headercontainer.addattrib("id","headercontainer")
		self.headercontainer.addattrib("style","{display:table-row;}")
		self.datacontainer = self.addcell(cell())
		self.datacontainer.addattrib("id","datacontainer")
		self.statusrow=""
		self.rowcount=0;
		self.colcount=0;

	def addcellat(self,x,y,incomingcell):
		""" add the incoming cell at row,col"""
		incomingcell.addattrib('style',"{display:table-cell}")
		if x < self.rowcount:
			#print "row:",x,"is within bounds"
			if y < self.colcount:
				#print "col:",y,"is within bounds"
				self.datacontainer.listofcells[x].listofcells[y]=incomingcell
				return incomingcell
			else:
				#print "y:",y,"is not within bounds"
				for i in range(y+1)[self.colcount:y+1]:
					addedcell=self.datacontainer.listofcells[x].addcell(cell())
					addedcell.addattrib('id',"col"+str(i))
				#header
				headercolcount = len(self.headercontainer)
				if headercolcount < y:
					for i in range(y+1)[headercolcount:y+1]:
						headercell=self.headercontainer.addcell(cell())
						headercell.addattrib('id',"col"+str(i))
						headercell.addattrib('style','{display:table-cell;}')
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
				rowcontainer=self.datacontainer.addcell(cell())
				rowcontainer.addattrib('id',"row"+str(i))
				rowcontainer.addattrib('style','{display:table-row;}')
				for j in range(colbounds):
					acell=rowcontainer.addcell(cell())
					acell.addattrib('id',"col"+str(j))
					acell.addattrib('style','{display:table-cell;}')

			self.rowcount += len(newrows)

			newcols=range(colbounds)[self.colcount:colbounds+1]

			#headerrow
			headercolcount=len(self.headercontainer)
			if headercolcount < y:
				newheadercols=range(colbounds)[headercolcount:colbounds+1]
				for j in newheadercols:
					headercell=self.headercontainer.addcell(cell())
					headercell.addattrib('id',"col"+str(j))
					headercell.addattrib('style','{display:table-cell;}')
			#headrow end

			if expandexistingrows:
				for i in existingrows:
					rowcontainer=self.datacontainer.listofcells[i]
					for j in newcols:
						acell=rowcontainer.addcell(cell())
						acell.addattrib("id","col"+str(j))
						acell.addattrib("style","{display:table-cell;}")
						#headercell=self.headercontainer.addcell(cell(cellid="col"+str(j)))
						#headercell.css.place.display="table-cell"

			self.colcount += len(newcols)

		self.datacontainer.listofcells[x].listofcells[y]=incomingcell
		return incomingcell

	def cellat(self,x,y):
			""" returns the cell at """
			return self.datacontainer.listofcells[x].listofcells[y]

	def html(self):
		return cell.html(self)
	
if __name__ == "__main__":
	#cond #1 atable = table(0,1)
	#cond #1 atable = table(0,1)
	atable = table()
	row=2;col=2;
	for i in range(row):
		for j in range(col):
			acell=cell("i:"+str(i)+"j:"+str(j))
			atable.addcellat(i,	j,acell)
	print atable.html()
