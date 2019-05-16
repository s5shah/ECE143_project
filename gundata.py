#Project ECE143
import pandas as pd 
import matplotlib.pyplot as plt

class gundata:
	'''
	A class which defines several functions to deal with gun violence data(mass shooting) 
	'''
	def __init__(self,year):
		assert isinstance(year,int),"invalid year"
		assert 2014<=year<=2018,"Only 2014-2018 mass shooting data available"
		self.data = pd.read_csv(f"dataset/ms{year}.csv")
		self.monthlist = {12:'Dec',11:'Nov',10:'Oct',9:'Sep',8:"Aug",7:"Jul",6:"Jun",5:"May",4:"Apr",3:"Mar",2:"Feb",1:"Jan"}

	def get_total_insidence(self,month=None):
		'''
		Return total number of mass gun shooting incidence
		If month=None will return total number of incidence in the whole year
		param:month
		type:int from 1 to 12, or a 2-dim list represents an interval of two months 
		return: int 
		'''
		assert isinstance(month,int) or isinstance(month,list) or isinstance(month,tuple) or month==None,"invalid input"
		if month == None:
			return len(self.data)

		if isinstance(month,int):
			assert 1<=month<=12
			return len(data.loc[self.data['Incident Date'].str.contains(self.monthlist[month])])

		if isinstance(month,list) or isinstance(month,tuple):
			assert len(month)==2,"invalid input"
			assert 1<=month[0]<= 12 and 1<=month[1]<=12 and month[0]<month[1],"invalid input"
			res = []
			for i in range(month[0],month[1]+1):
				res.append(len(self.data.loc[self.data['Incident Date'].str.contains(self.monthlist[i])]))
			return res

	#To be updated,sum

	





