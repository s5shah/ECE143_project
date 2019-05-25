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
		#plt.figure()
		x2014 = self.data2014.get_total_insidence()
		x2015 = self.data2015.get_total_insidence()
		x2016 = self.data2016.get_total_insidence()
		x2017 = self.data2017.get_total_insidence()
		x2018 = self.data2018.get_total_insidence()
		x2019 = self.data2019.get_total_insidence()
		plt.plot(['2014','2015','2016','2017','2018'],[x2014,x2015,x2016,x2017,x2018],marker='o',label=self.datatype)
		plt.xlabel('Year') # apply labels
		plt.ylabel(f'Nunber of {self.datatype}')
		#plt.title(f'Number of {self.datatype} per year(2014-2018)')
		#plt.show()
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
		ylabel.append('others_ave')
		ylabel.reverse()
		y_pos = np.arange(11)
		performance = list(state_dict.values())[0:10]
		performance.append((len(state.data)-sum(performance))/(len(state_dict)-10))
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


	def plot_school_type(self):
		assert self.datatype == 'School_Schootings', "input is not school shooting data"
		school_type = self.dataall.count_by_colume('School Type')
		performance = list(school_type.values())
		ylabel = list(school_type.keys())
		y_pos = np.arange(len(ylabel))
		plt.bar(ylabel,performance)
		print(y_pos,ylabel)
		#plt.xticks(y_pos,ylabel)
		
		plt.title("count school type")
		#plt.legend()

		plt.show()
	def plot_school_type_per_year(self):
		assert self.datatype == 'School_Schootings', "input is not school shooting data"
		x2014 = self.data2014.count_by_colume('School Type')
		x2015 = self.data2015.count_by_colume('School Type')
		x2016 = self.data2016.count_by_colume('School Type')
		x2017 = self.data2017.count_by_colume('School Type')
		x2018 = self.data2018.count_by_colume('School Type')
		x2019 = self.data2019.count_by_colume('School Type')
		l = 5
		v2014 = [x2014['College or University'],x2014['High School'],x2014['Middle School'],x2014['Elementary School'],x2014['K-12 School']]
		v2015 = [x2015['College or University'],x2015['High School'],x2015['Middle School'],x2015['Elementary School'],x2015['K-12 School']]
		v2016 = [x2016['College or University'],x2016['High School'],x2016['Middle School'],x2016['Elementary School'],x2016['K-12 School']]
		v2017 = [x2017['College or University'],x2017['High School'],x2017['Middle School'],x2017['Elementary School'],x2017['K-12 School']]
		v2018 = [x2018['College or University'],x2018['High School'],x2018['Middle School'],x2018['Elementary School'],x2018['K-12 School']]
		v2019 = [x2019['College or University'],x2019['High School'],x2019['Middle School'],x2019['Elementary School'],x2019['K-12 School']]
		w = 0.1
		print(x2014.keys() ,x2015.keys(),x2016.keys(),x2017.keys(),x2018.keys())

		y_pos = np.arange(l)
		plt.bar(y_pos,v2014,w,label='2014')
		plt.bar(y_pos+0.1,v2015,w,label='2015')
		plt.bar(y_pos+0.2,v2016,w,label='2016')
		plt.bar(y_pos+0.3,v2017,w,label='2017')
		plt.bar(y_pos+0.4,v2018,w,label='2018')
		plt.bar(y_pos+0.5,v2019,w,label='2019.5.15')
		plt.xticks(y_pos,['College/University','High School','Middle School','Elementary School','K-12 School'])
		plt.title('schooltype varies per year')
		plt.legend()
		plt.show()



		

		



if __name__=="__main__":

	data1 = data("Mass_Shootings")
	data2 = data("Officers_Shootings")
	data3 = data("School_Schootings")
	data1.plot_incidence_per_year()
	data2.plot_incidence_per_year()
	data3.plot_incidence_per_year()
	plt.title(f'Number of mass/officers/school shootings per year(2014-2018)')
	plt.legend()
	plt.show()
	



	#analyze mass shootings
	data1.plot_incidence_per_year()
	plt.title(f'Number of {data1.datatype} per year(2014-2018)')
	plt.show()
	data1.plot_incidence_per_month()
	fig,ax = plt.subplots()
	data1.plot_state_year()
	#analyze officers shootings
	data2.plot_incidence_per_year()
	plt.title(f'Number of {data2.datatype} per year(2014-2018)')
	plt.show()
	data2.plot_incidence_per_month()
	fig,ax = plt.subplots()
	data2.plot_state_year()
	

    #analyze school shootings
	data3.plot_incidence_per_year()
	plt.title(f'Number of {data3.datatype} per year(2014-2018)')
	plt.show()
	data3.plot_incidence_per_month()
	fig,ax = plt.subplots()
	data3.plot_state_year()
	

	data3.plot_school_type()
	data3.plot_school_type_per_year()
	
	
	

