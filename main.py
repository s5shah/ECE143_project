#project ECE143
import matplotlib.pyplot as plt
import numpy as np
from gundata import gundata

class data:
	def __init__(self,datatype):
		self.datatype = datatype
		self.data2014 = gundata(datatype,2014)
		self.data2015 = gundata(datatype,2015)
		self.data2016 = gundata(datatype,2016)
		self.data2017 = gundata(datatype,2017)
		self.data2018 = gundata(datatype,2018)
		self.data2019 = gundata(datatype,2019)


	def plot_incidence_per_year(self):
		plt.figure()
		x2014 = self.data2014.get_total_insidence()
		x2015 = self.data2015.get_total_insidence()
		x2016 = self.data2016.get_total_insidence()
		x2017 = self.data2017.get_total_insidence()
		x2018 = self.data2018.get_total_insidence()
		x2019 = self.data2019.get_total_insidence()
		plt.plot(['2014','2015','2016','2017','2018'],[x2014,x2015,x2016,x2017,x2018])
		plt.xlabel('Year') # apply labels
		plt.ylabel(f'Nunber of {self.datatype}')
		plt.title(f'Number of {self.datatype} per year(2014-2018)')
		plt.show()
	def plot_incidence_per_month(self):
		from matplotlib.pylab import subplots
		fig,ax=subplots()
		x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
		x2014 = np.array(self.data2014.get_total_insidence([1,12]))
		x2015 = np.array(self.data2015.get_total_insidence([1,12]))
		x2016 = np.array(self.data2016.get_total_insidence([1,12]))
		x2017 = np.array(self.data2017.get_total_insidence([1,12]))
		x2018 = np.array(self.data2018.get_total_insidence([1,12]))
		x2019 = np.array(self.data2019.get_total_insidence([1,12]))
		ave = (x2014+x2015+x2016+x2017+x2018)/5
		ax.plot(x,x2014,x,x2015,x,x2016,x,x2017,x,x2018,x,x2019,x,ave,'--or')
		plt.title(f'Number of {self.datatype} per month(2014-2019.5.14)')
		ax.legend(('2014','2015','2016','2017','2018','2019','ave'),loc='best')
		plt.show()







if __name__=="__main__":
	data1 = data("Mass_Shootings")
	data1.plot_incidence_per_year()
	data1.plot_incidence_per_month()

	data2 = data("Officers_Shootings")
	data2.plot_incidence_per_year()
	data2.plot_incidence_per_month()


	data3 = data("School_Schootings")
	data3.plot_incidence_per_year()
	data3.plot_incidence_per_month()
	

