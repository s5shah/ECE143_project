#project ECE143
import matplotlib.pyplot as plt
from gundata import gundata

class data:
	def __init__(self):
		self.data2014 = gundata(2014)
		self.data2015 = gundata(2015)
		self.data2016 = gundata(2016)
		self.data2017 = gundata(2017)
		self.data2018 = gundata(2018)


	def plot_incidence_per_year(self):
		plt.figure()
		x2014 = self.data2014.get_total_insidence()
		x2015 = self.data2015.get_total_insidence()
		x2016 = self.data2016.get_total_insidence()
		x2017 = self.data2017.get_total_insidence()
		x2018 = self.data2018.get_total_insidence()
		plt.plot(['2014','2015','2016','2017','2018'],[x2014,x2015,x2016,x2017,x2018])
		plt.xlabel('Year') # apply labels
		plt.ylabel('Nunber of mass shooting')
		plt.title('Number of mass shooting per year')
		plt.show()
	def plot_incidence_per_month(self):
		from matplotlib.pylab import subplots
		fig,ax=subplots()
		x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
		x2014 = self.data2014.get_total_insidence([1,12])
		x2015 = self.data2015.get_total_insidence([1,12])
		x2016 = self.data2016.get_total_insidence([1,12])
		x2017 = self.data2017.get_total_insidence([1,12])
		x2018 = self.data2018.get_total_insidence([1,12])
		ax.plot(x,x2014,x,x2015,x,x2016,x,x2017,x,x2018,'or--')
		ax.title('Number of mass shooting per month(2014-2018)')
		ax.legend(('2014','2015','2016','2017','2018'),loc='best')





if __name__=="__main__":
	data1 = data()
	data1.plot_incidence_per_year()
	data1.plot_incidence_per_month()
	

