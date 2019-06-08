import pandas as pd 

class gundata:
    '''
    A class which defines several functions to extract data from the data sets. 
    '''
    def __init__(self,df,datatype):
        '''
        Initialize some self variables which will be passed into the functions.
        df is the dataframe of the csv imported
        datatype is the type of gun violence being analyzed
        '''
        assert isinstance(df,pd.core.frame.DataFrame)
        assert isinstance(datatype, str)
        assert datatype in ['Mass_Shootings', 'School_Shootings', 'Officers_Shootings']
        
        self.datatype = datatype
        self.data = df
        self.monthlist = {12:'Dec',11:'Nov',10:'Oct',9:'Sep',8:"Aug",7:"Jul",6:"Jun",5:"May",4:"Apr",3:"Mar",2:"Feb",1:"Jan"}

    def get_total_incidents(self):
        '''
        Takes in input as self and uses that to count the number of incidents.
        Returns the total number of incidents from the provided data.
        The function returns an integer.
        '''
        assert isinstance(self.data, pd.core.frame.DataFrame)

        return len(self.data)

    def count_by_columns(self,col):
        '''
        Takes in self and a str col (column name).
        Returns a dictionary with a count of every entry in the column passed in.
        For example, this function will return a dictionary with a count of incidents in every state if the column passed in was 'State'.
        '''
        assert col in self.data.columns
        assert isinstance(self.data, pd.core.frame.DataFrame)
        
        return dict(self.data[col].value_counts())

    def count_casualties(self):
        '''   
        Takes in input as self to count the number of casualties for self.data
        Returns the total number of casualties that occured for a data set.
        This function only works for Mass Shootings and Officers Shootings events.
        So, the self.datatype should be either Mass_Shootings or Officers_Shootings.
        '''
        assert isinstance(self.data, pd.core.frame.DataFrame)
        assert isinstance(self.datatype, str)
        assert self.datatype in ['Mass_Shootings','Officers_Shootings']
        
#        self.data['casualities']=self.data['# killed']+self.data['# injured']
        return self.data['# injured'].sum() + self.data['# killed'].sum()
        
    def create_casualties(self):
        '''
        Takes in input as self to create a column with the casualty count for each incident.
        Returns a new dataframe with a column of casualties.
        This function can be used in combination of the other function to get the number of casualties for different states, etc.
        '''
        assert self.datatype in ['Mass_Shootings','Officers_Shootings'],'School shooting does not have casualties'
        
        self.data['casualties']=self.data['# killed']+self.data['# injured']
        return self.data
        
    def casualties_per_state(self):
        '''
        Takes in input as self to create a dictionary of state wise casualties for officer shootings.
        Returns a dictionary of state wise casualties for Officers Shootings
        '''
        assert self.datatype == 'Officers_Shootings'
        
        grouped = self.data.groupby('State')
        casualties = dict()
        for i in grouped.groups:
            group = grouped.get_group(i)
            casualties[i] = group['# killed'].sum() + group['# injured'].sum()
                      
        return casualties