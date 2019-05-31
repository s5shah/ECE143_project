#project ECE143
import matplotlib.pyplot as plt
import numpy as np
from gundata import gundata
import pandas as pd
import holoviews as hv
from matplotlib.widgets import Slider, Button, RadioButtons
hv.extension('bokeh')

class data:
    def __init__(self,datatype):
        '''
        initialize and load data
        param:
            datatype: class of shooting type within ''Mass_Shootings','Officers_Shootings','School_Shootings'
        '''
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


    def plot_incidence_per_year(self,method='line'):
        '''
        plot the number of incidence changing with years
        param:
            method: default='line': plot in line style, 'bar': plot in bar style
        '''
        #plt.figure()
        assert method in ['line','bar'],'invalid method'
        x2014 = self.data2014.get_total_insidence()
        x2015 = self.data2015.get_total_insidence()
        x2016 = self.data2016.get_total_insidence()
        x2017 = self.data2017.get_total_insidence()
        x2018 = self.data2018.get_total_insidence()
        if method == 'bar':
            plt.bar(['2014','2015','2016','2017','2018'],[x2014,x2015,x2016,x2017,x2018],label=self.datatype)
        else:
            plt.plot(['2014','2015','2016','2017','2018'],[x2014,x2015,x2016,x2017,x2018],marker='o',label=self.datatype)


        plt.xlabel('Year') # apply labels
        plt.ylabel(f'Nunber of {self.datatype}')
        plt.title(f'Number of {self.datatype} per year(2014-2018)')
        plt.show()
        
    def plot_casualties_per_year(self,method='line'):
        '''
        plot casualties of incidence changing with years
        param:
            method: default='line': plot in line style, 'bar': plot in bar style
        '''
        assert method in ['line','bar'],'invalid method'
        plt.figure()
        x2014 = self.data2014.count_casualties()
        x2015 = self.data2015.count_casualties()
        x2016 = self.data2016.count_casualties()
        x2017 = self.data2017.count_casualties()
        x2018 = self.data2018.count_casualties()
        assert self.datatype in ['Mass_Shootings','Officers_Shootings'],'Cannot plot casualties of School shooting'
        if method == 'bar':
            plt.bar(['2014','2015','2016','2017','2018'],[x2014,x2015,x2016,x2017,x2018],label=self.datatype)
        else:
            plt.plot(['2014','2015','2016','2017','2018'],[x2014,x2015,x2016,x2017,x2018],marker='o',label=self.datatype)
        plt.show()

    def plot_incidence_and_casualties_per_year(self,method = 'line'):
        '''
        combine the former two function
        '''
        assert method in ['line','bar'],'invalid method'
        x2014 = self.data2014.get_total_insidence()
        x2015 = self.data2015.get_total_insidence()
        x2016 = self.data2016.get_total_insidence()
        x2017 = self.data2017.get_total_insidence()
        x2018 = self.data2018.get_total_insidence()
        xpos = np.arange(5)
        if method == 'bar':
            plt.bar(xpos,[x2014,x2015,x2016,x2017,x2018],0.4,label='number of incidence')
        else:
            plt.plot(['2014','2015','2016','2017','2018'],[x2014,x2015,x2016,x2017,x2018],marker='o',label='number of incidence')
        x2014 = self.data2014.count_casualties()
        x2015 = self.data2015.count_casualties()
        x2016 = self.data2016.count_casualties()
        x2017 = self.data2017.count_casualties()
        x2018 = self.data2018.count_casualties()
        assert self.datatype in ['Mass_Shootings','Officers_Shootings'],'Cannot plot casualties of School shooting'
        if method == 'bar':
            plt.bar(xpos+0.4,[x2014,x2015,x2016,x2017,x2018],0.4,label='number of casualties')
        else:
            plt.plot(['2014','2015','2016','2017','2018'],[x2014,x2015,x2016,x2017,x2018],marker='o',label='number of casualties')
        plt.xticks(xpos+0.2,['2014','2015','2016','2017','2018'])

        plt.xlabel('Year') # apply labels
        plt.ylabel(f'Nunber')
        plt.title(f'Number of {self.datatype} per year(2014-2018)')
        plt.legend()
        plt.show()


        

    def plot_incidence_per_month(self):
        '''
        plot number of incidence changing within a specific year
        '''
        from matplotlib.pylab import subplots
        fig,ax = subplots()
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
        
    def plot_casualties_per_month(self):
        '''
        plot casualties of incidence changing within a specific year
        '''
        from matplotlib.pylab import subplots
        fig,ax = subplots()
        x = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
        x2014 = np.array(self.data2014.count_casualties([1,12]))
        x2015 = np.array(self.data2015.count_casualties([1,12]))
        x2016 = np.array(self.data2016.count_casualties([1,12]))
        x2017 = np.array(self.data2017.count_casualties([1,12]))
        x2018 = np.array(self.data2018.count_casualties([1,12]))
        x2019 = np.array(self.data2019.count_casualties([1,12]))
        assert self.datatype in ['Mass_Shootings','Officers_Shootings'],'Cannot plot casualties of School shooting'
        ave = (x2014+x2015+x2016+x2017+x2018)/5
        ax.plot(x,x2014,x,x2015,x,x2016,x,x2017,x,x2018,x,x2019,x,ave,'--or')
        plt.title(f'Casualties of {self.datatype} per month(2014-2019.5.14)')
        ax.legend(('2014','2015','2016','2017','2018','2019','ave'),loc='best')
        plt.show()
    
    
    
    def plot_state_year_update(self,t):
        '''
        plot numbers of incidence of ten states which contribute most incidence and the average
        number of incidence of states excluding the hightest ten
        param:
            t: year deviate from 2014, automatically filled by functionplot_state_year
        '''
        fig = plt.figure()
        state = [self.data2014,self.data2015,self.data2016,self.data2017,self.data2018,self.data2019][t]
        fig,ax = plt.subplots()

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

        

    def plot_state_year(self,year= None):
        '''
        plot pie chart showing how the ten highest state and the other states contribute
        to the total number of incidence 
        '''
        
        #ani = animation.FuncAnimation(fig, update,frames=800)
        
        '''
        for t in range(6):
            self.plot_state_year_update(t)
            plt.pause(1)
        '''
        fig,ax = plt.subplots()
        if year == None:
            state_dict = self.dataall.count_by_colume('State')
        if year == 2014:
            state_dict = self.data2014.count_by_colume('State')
        if year == 2015:
            state_dict = self.data2014.count_by_colume('State')
        if year == 2016:
            state_dict = self.data2014.count_by_colume('State')
        if year == 2017:
            state_dict = self.data2014.count_by_colume('State')
        if year == 2018:
            state_dict = self.data2014.count_by_colume('State')
        if year == 2019:
            state_dict = self.data2014.count_by_colume('State')
        x = list(state_dict.values())[0:10]
        x.append(sum(list(state_dict.values())[10:]))

        labels = list(state_dict.keys())[0:10] 
        labels.append('others')
        #print(len(x),len(labels))
        ax.clear()
        ax.pie(x = x,labels = labels,labeldistance=1.1,autopct = '%3.2f%%',colors=['#FF0400','#FFFC00','#45D304','#07D09C','#36D3FD','#2C02FE','#FD02FE','#FC50D8','#F18EB1','#D0D6D5','#eeefff'])
        ax.set_title(f"{self.datatype}(2014-2019.5.14)")
        #plt.pause(0)



    def plot_state_casualties_update(self,t):
        '''
        plot casualties of ten states which causes most casualties and average of casualties of states
        excluding the hightest ten
        param:
            t: year deviate from 2014, automatically filled by functionplot_state_year
        '''
        print(type(self.data2014))
        self.data2014_c=self.data2014.create_casualties()
        self.data2015_c=self.data2015.create_casualties()
        self.data2016_c=self.data2016.create_casualties()
        self.data2017_c=self.data2017.create_casualties()
        self.data2018_c=self.data2018.create_casualties()
        self.data2019_c=self.data2019.create_casualties()
        fig,ax = plt.subplots()
        state = [self.data2014_c,self.data2015_c,self.data2016_c,self.data2017_c,self.data2018_c,self.data2019_c][t]
        state_dict = state.groupby('State')
        data_dict={}
        for group,data in state_dict:
            data_dict[group]=data['casualties'].sum()
        data_list=sorted(data_dict.items(),key=lambda item:item[1],reverse=True)
        ylabel = []
        yvalue = []
        for key in data_list:
            ylabel.append(key[0])
            yvalue.append(key[1])
        ylabel.insert(10,'others_ave')
        y_pos = np.arange(11)
        performance = yvalue[0:10]
        performance.insert(10,(sum(yvalue[10:-1]))/(len(yvalue)-10))
        performance.reverse()
        error = np.random.rand(11)
        ylabel=ylabel[0:11]
        ylabel.reverse()
        ax.clear()
        ax.barh(y_pos, performance, alpha=1)
        ax.set_yticks(ticks=y_pos)
        ax.set_yticklabels(labels=ylabel)
        ax.set_title(f"{self.datatype}_{t+2014}")
        #ax.set_alpha()
        
    def plot_state_year_casualties(self):
        '''
        plot pie chart showing how the ten highest state and the other states contribute
        to the total number of casualties
        '''
        #ani = animation.FuncAnimation(fig, update,frames=800)
        assert self.datatype in ['Mass_Shootings','Officers_Shootings'],'Cannot plot casualties of School shooting'
        for t in range(6):
            self.plot_state_casualties_update(t)
            plt.pause(1)
        fig,ax = plt.subplots()
        
        self.dataall_c=self.dataall.create_casualties()
        state =self.dataall_c
        state_dict = state.groupby('State')
        data_dict={}
        for group,data in state_dict:
            data_dict[group]=data['casualties'].sum()
        data_list=sorted(data_dict.items(),key=lambda item:item[1],reverse=True)
        ylabel = []
        yvalue = []
        for key in data_list:
            ylabel.append(key[0])
            yvalue.append(key[1])
        ylabel.insert(10,'others_ave')
        performance = yvalue[0:10]
        performance.insert(10,(sum(yvalue[10:-1])))
        ylabel=ylabel[0:11]
        #print(len(x),len(labels))
        ax.clear()
        ax.pie(x = performance,labels = ylabel,labeldistance=1.1,autopct = '%3.2f%%')
        ax.set_title(f"{self.datatype}_Casualties(2014-2019.5.14)")




    def plot_school_type(self):
        '''
        plot bar chart showing the number of incidences happened at different types of school
        '''
        assert self.datatype == 'School_Schootings', "input is not school shooting data"
        school_type = self.dataall.count_by_colume('School Type')
        performance = list(school_type.values())
        ylabel = list(school_type.keys())
        y_pos = np.arange(len(ylabel))
        plt.bar(ylabel,performance)
        #print(y_pos,ylabel)
        #plt.xticks(y_pos,ylabel)
        
        plt.title("count school type")
        #plt.legend()

        plt.show()
    def plot_school_type_per_year(self):
        '''
        plot bar chart showing the number of incidences happened at different types of school within a specific year
        '''
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
        #print(x2014.keys() ,x2015.keys(),x2016.keys(),x2017.keys(),x2018.keys())

        y_pos = np.arange(l)
        plt.bar(y_pos,v2014,w,label='2014')
        plt.bar(y_pos+0.1,v2015,w,label='2015')
        plt.bar(y_pos+0.2,v2016,w,label='2016')
        plt.bar(y_pos+0.3,v2017,w,label='2017')
        plt.bar(y_pos+0.4,v2018,w,label='2018')
        plt.bar(y_pos+0.5,v2019,w,label='2019.5.15')
        plt.xticks(y_pos+0.2,['University','High Sch','Middle Sch','Elementary Sch','K-12 Sch'])
        plt.title('schooltype varies per year')
        plt.legend()
        plt.show()

    def plot_state_year_hv(self,year= None):
        '''
        plot pie chart showing how the ten highest state and the other states contribute
        to the total number of incidence 
        '''
        
        #ani = animation.FuncAnimation(fig, update,frames=800)
        
        '''
        for t in range(6):
            self.plot_state_year_update(t)
            plt.pause(1)
        '''
        fig,ax = plt.subplots()
        if year == None:
            state_dict = self.dataall.count_by_colume('State')
        if year == 2014:
            state_dict = self.data2014.count_by_colume('State')
        if year == 2015:
            state_dict = self.data2015.count_by_colume('State')
        if year == 2016:
            state_dict = self.data2016.count_by_colume('State')
        if year == 2017:
            state_dict = self.data2017.count_by_colume('State')
        if year == 2018:
            state_dict = self.data2018.count_by_colume('State')
        if year == 2019:
            state_dict = self.data2019.count_by_colume('State')
        x = list(state_dict.values())[0:10]
        x.append(sum(list(state_dict.values())[10:]))

        labels = list(state_dict.keys())[0:10] 
        labels.append('others')
        #print(len(x),len(labels))
    def top5(self, b5):
        assert isinstance(b5,list)
        state_dict_2014 = self.data2014.count_by_colume('State')
        state_dict_2015 = self.data2015.count_by_colume('State')
        state_dict_2016 = self.data2016.count_by_colume('State')
        state_dict_2017 = self.data2017.count_by_colume('State')
        state_dict_2018 = self.data2018.count_by_colume('State')
        state_dict_2019 = self.data2019.count_by_colume('State')
        x2014 = []
        x2015 = []
        x2016 = []
        x2017 = []
        x2018 = []
        x2019 = []
        for i in range(len(b5)):
            if b5[i] in state_dict_2014:
                x2014.append(state_dict_2014[b5[i]]/self.data2014.get_total_insidence())
            else:
                x2014.append(0)
            if b5[i] in state_dict_2015:
                x2015.append(state_dict_2015[b5[i]]/self.data2015.get_total_insidence())
            else:
                x2015.append(0)
            if b5[i] in state_dict_2016:
                x2016.append(state_dict_2016[b5[i]]/self.data2016.get_total_insidence())
            else:
                x2016.append(0)
            if b5[i] in state_dict_2017:
                x2017.append(state_dict_2017[b5[i]]/self.data2017.get_total_insidence())
            else:
                x2017.append(0)
            if b5[i] in state_dict_2018:
                x2018.append(state_dict_2018[b5[i]]/self.data2018.get_total_insidence())
            else:
                x2018.append(0)
            if b5[i] in state_dict_2019:
                x2019.append(state_dict_2019[b5[i]]/self.data2019.get_total_insidence())
            else:
                x2019.append(0)
        a2014 = pd.DataFrame(index = np.arange(5),data = {'state':b5,'percentage' :x2014,'year':2014})
        a2015 = pd.DataFrame(index = np.arange(5),data = {'state':b5,'percentage' :x2015,'year':2015})
        a2016 = pd.DataFrame(index = np.arange(5),data = {'state':b5,'percentage' :x2016,'year':2016})
        a2017 = pd.DataFrame(index = np.arange(5),data = {'state':b5,'percentage' :x2017,'year':2017})
        a2018 = pd.DataFrame(index = np.arange(5),data = {'state':b5,'percentage' :x2018,'year':2018})
        a2019 = pd.DataFrame(index = np.arange(5),data = {'state':b5,'percentage' :x2019,'year':2019})
        b= pd.concat([a2014,a2015,a2016,a2017,a2018,a2019])
        edata = hv.Dataset(data=b,kdims=['state'])
        edata.to(hv.Bars,'state','percentage',groupby='year').options(height=200)
        return edata
    def top10_pie(self):
        global ax,fig,risk
        state_dict = self.data2014.count_by_colume('State')
        x = list(state_dict.values())[0:10]
        x.append(sum(list(state_dict.values())[10:]))
        labels = list(state_dict.keys())[0:10] 
        labels.append('others')
        fig, ax = plt.subplots(2)

        # draw the initial pie chart
        ax[0].pie(x = x,labels = labels,labeldistance=1.1,autopct = '%3.2f%%',colors=['#FF0400','#FFFC00','#45D304','#07D09C','#36D3FD','#2C02FE','#FD02FE','#FC50D8','#F18EB1','#D0D6D5','#eeefff'])
        ax[0].set_position([0.25,0.4,.6,.6])

        # create the slider
        ax[1].set_position([0.25, 0.35, 0.5, 0.03])
        risk = Slider(ax[1], 'year',2014, 2019, valinit=2014,valstep=1,valfmt='%0.0f')

        risk.on_changed(self.update)
        plt.show()


    def update(self,val):
        ax[0].clear()
        year = int(risk.val)
        #print(year)
        
        if year == None:
            state_dict = self.dataall.count_by_colume('State')
        if year == 2014:
            state_dict = self.data2014.count_by_colume('State')
        if year == 2015:
            state_dict = self.data2015.count_by_colume('State')
        if year == 2016:
            state_dict = self.data2016.count_by_colume('State')
        if year == 2017:
            state_dict = self.data2017.count_by_colume('State')
        if year == 2018:
            state_dict = self.data2018.count_by_colume('State')
        if year == 2019:
            state_dict = self.data2019.count_by_colume('State')
        x = list(state_dict.values())[0:10]
        x.append(sum(list(state_dict.values())[10:]))

        labels = list(state_dict.keys())[0:10] 
        labels.append('others')
        ax[0].pie(x = x,labels = labels,labeldistance=1.1,autopct = '%3.2f%%',colors=['#FF0400','#FFFC00','#45D304','#07D09C','#36D3FD','#2C02FE','#FD02FE','#FC50D8','#F18EB1','#D0D6D5','#eeefff'])
        fig.canvas.draw_idle()









if __name__=="__main__":
    
    data1 = data("Mass_Shootings")
    data2 = data("Officers_Shootings")
    data3 = data("School_Schootings")
    data1.plot_incidence_per_year(method='bar') 
    data1.plot_casualties_per_year(method='bar')
    data2.plot_incidence_per_year(method='bar') 
    data2.plot_casualties_per_year(method='bar')
    #data1.plot_casualties_per_month()
    #data1.plot_state_year()
    #data1.plot_state_year_casualties()
    
    '''
    plt.title(f'Number of mass/officers/school shootings per year(2014-2018)')
    plt.legend()
    plt.show()
    '''



    #analyze mass shootings
    '''
    data1.plot_incidence_per_year()
    plt.title(f'Number of {data1.datatype} per year(2014-2018)')
    plt.show()
    data1.plot_incidence_per_month()
    
    fig,ax = plt.subplots()
    data1.plot_state_year()
    '''
    '''
    #analyze officers shootings
    data2.plot_incidence_per_year()
    plt.title(f'Number of {data2.datatype} per year(2014-2018)')
    plt.show()
    data2.plot_incidence_per_month()
    fig,ax = plt.subplots()
    data2.plot_state_year()
    '''
    '''
    #analyze school shootings
    data3.plot_incidence_per_year()
    plt.title(f'Number of {data3.datatype} per year(2014-2018)')
    plt.show()
    data3.plot_incidence_per_month()
    fig,ax = plt.subplots()
    data3.plot_state_year()
    '''
    '''
    data3.plot_school_type()
    data3.plot_school_type_per_year()
    '''
    
    
