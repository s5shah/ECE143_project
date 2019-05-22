#project ECE143
import matplotlib.pyplot as plt
import numpy as np
from gundata import gundata
import pandas as pd

class data:
	def __init__(self,datatype):
		self.datatype = datatype
		x2014 =pd.read_csv(f"Scrape/{datatype}_2014.csv")
		x2015 =pd.read_csv(f"Scrape/{datatype}_2015.csv")
		x2016 =pd.read_csv(f"Scrape/{datatype}_2016.csv")
		x2017 =pd.read_csv(f"Scrape/{datatype}_2017.csv")
		x2018 =pd.read_csv(f"Scrape/{datatype}_2018.csv")
		x2019 =pd.read_csv(f"Scrape/{datatype}_2019.csv")
		self.data2014 = gundata(x2014,datatype)
		self.data2015 = gundata(x2015,datatype)
		self.data2016 = gundata(x2016,datatype)
		self.data2017 = gundata(x2017,datatype)
		self.data2018 = gundata(x2018,datatype)
		self.data2019 = gundata(x2019,datatype)
		a = pd.concat([x2014,x2015,x2016,x2017,x2018,x2019])
		self.dataall = gundata(a,datatype)


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

	def plot_state_year_update(self,t):
		#fig = plt.figure()
		state = [self.data2014,self.data2015,self.data2016,self.data2017,self.data2018,self.data2019][t]
		#fig,ax = plt.subplots()

		state_dict = state.count_by_colume('State')
		ylabel = list(state_dict.keys())[0:10]
		ylabel.append('others')
		ylabel.reverse()
		y_pos = np.arange(11)
		performance = list(state_dict.values())[0:10]
		performance.append(len(state.data)-sum(performance))
		performance.reverse()
		error = np.random.rand(11)
		ax.clear()
		ax.barh(y_pos, performance, alpha=1)
		ax.set_yticks(ticks=y_pos)
		ax.set_yticklabels(labels=ylabel)
		ax.set_title(f"{state.datatype}_{t+2014}")
		#ax.set_alpha()

		

	def plot_state_year(self):
		
		#ani = animation.FuncAnimation(fig, update,frames=800)
		
		for t in range(6):
			self.plot_state_year_update(t)
			plt.pause(1)
		state_dict = self.dataall.count_by_colume('State')
		x = list(state_dict.values())[0:10]
		x.append(sum(list(state_dict.values())[10:]))

		labels = list(state_dict.keys())[0:10] 
		labels.append('others')
		#print(len(x),len(labels))
		ax.clear()
		ax.pie(x = x,labels = labels,labeldistance=1.1,autopct = '%3.2f%%')
		ax.set_title(f"{self.datatype}(2014-2019.5.14)")
		plt.pause(5)
		
		

		








if __name__=="__main__":
	data1 = data("Mass_Shootings")
	data1.plot_incidence_per_year()
	data1.plot_incidence_per_month()
	fig,ax = plt.subplots()
	data1.plot_state_year()

	
	data2 = data("Officers_Shootings")
	data2.plot_incidence_per_year()
	data2.plot_incidence_per_month()
	fig,ax = plt.subplots()
	data2.plot_state_year()


	data3 = data("School_Schootings")
	data3.plot_incidence_per_year()
	data3.plot_incidence_per_month()
	fig,ax = plt.subplots()
	data3.plot_state_year()
	
	
	

