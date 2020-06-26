import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import pymysql
from sqlalchemy import create_engine


#saws the amount of tourists yearly in Greece from 2011 - 2015
def sum_period():
    #establishing connections for data base
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xxxx",
    auth_plugin='mysql_native_password',
    database="PythonProject"
    )
    engine = create_engine('mysql+pymysql://root:pao134ever@localhost:3306/PythonProject', echo = False)
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS periodsum")
    mycursor.execute("CREATE DATABASE IF NOT EXISTS PythonProject")
    mycursor.execute("CREATE TABLE IF NOT EXISTS periodsum (tourists BIGINT, periods TEXT, years INT, months VARCHAR(255), PRIMARY KEY(years,months) )")

    #these are the months for the separation of the year 
    months1 = ['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΙ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠ','ΟΚΤ','ΝΟΕ','ΔΕΚ']
    months2 = ['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΙΟΣ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠΤ','ΟΚΤ','ΝΟΕΜ','ΔΕΚ']
    months3 = ['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΙΟΣ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠ','ΟΚΤ','ΝΟΕ','ΔΕΚ']
    months4 = ['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΙ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠΤ','ΟΚΤ','ΝΟΕΜ','ΔΕΚ']
    
    for period in range(1,5):
        for year in range(2011, 2015):
            name_id =str(year) + "-Q" + str(4)
            if year==2011:    
                excel_file1 = name_id + '.xls'     
                #reading the right rows from each sheet of the excels and add columns for period and year
                data_m1 = pd.read_excel(excel_file1, sheet_name= months1[(period*3)-3],  skiprows= 65, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m1.insert(1, "Period", months1[(period*3)-3])                
                data_m1.insert(2, "Year", year)
                data_m2 = pd.read_excel(excel_file1, sheet_name= months1[(period*3)-2],  skiprows= 65, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m2.insert(1, "Period", months1[(period*3)-2])                
                data_m2.insert(2, "Year", year)
                data_m3 = pd.read_excel(excel_file1, sheet_name= months1[(period*3)-1],  skiprows= 65, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m3.insert(1, "Period", months1[(period*3)-1])                
                data_m3.insert(2, "Year", year)
                #concat the 3 months of each period
                data_all_Q_2011 = pd.concat([data_m1, data_m2, data_m3])
            if year==2012:    
                excel_file2 = name_id + '.xls'     
                #reading the right rows from each sheet of the excels and add columns for period and year
                data_m1 = pd.read_excel(excel_file2, sheet_name= months2[(period*3)-3],  skiprows= 65, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m1.insert(1, "Period", months2[(period*3)-3])                
                data_m1.insert(2, "Year", year)
                data_m2 = pd.read_excel(excel_file2, sheet_name= months2[(period*3)-2],  skiprows= 65, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m2.insert(1, "Period", months2[(period*3)-2])                
                data_m2.insert(2, "Year", year)
                data_m3 = pd.read_excel(excel_file2, sheet_name= months2[(period*3)-1],  skiprows= 65, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m3.insert(1, "Period", months2[(period*3)-1])                
                data_m3.insert(2, "Year", year)
                #concat the 3 months of each period
                data_all_Q_2012 = pd.concat([data_m1, data_m2, data_m3])
            if year==2013:    
                excel_file3 = name_id + '.xls'
                #due to lack of similarity between the sheets, use dynamic values for row skipping    
                skipRows = 65        
                if (period==1 or period==2):
                    skipRows = 64  
                #reading the right rows from each sheet of the excels and add columns for period and year
                data_m1 = pd.read_excel(excel_file3, sheet_name= months3[(period*3)-3],  skiprows= skipRows, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m1.insert(1, "Period", months3[(period*3)-3])                
                data_m1.insert(2, "Year", year)
                data_m2 = pd.read_excel(excel_file3, sheet_name= months3[(period*3)-2],  skiprows= skipRows, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m2.insert(1, "Period", months3[(period*3)-2])                
                data_m2.insert(2, "Year", year)
                data_m3 = pd.read_excel(excel_file3, sheet_name= months3[(period*3)-1],  skiprows= skipRows, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m3.insert(1, "Period", months3[(period*3)-1])                
                data_m3.insert(2, "Year", year)
                #concat the 3 months of each period
                data_all_Q_2013 = pd.concat([data_m1, data_m2, data_m3])
            if year==2014:    
                excel_file4 = name_id + '.xls'     
                #reading the right rows from each sheet of the excels and add columns for period and year
                data_m1 = pd.read_excel(excel_file4, sheet_name= months4[(period*3)-3],  skiprows= 65, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m1.insert(1, "Period", months4[(period*3)-3])                
                data_m1.insert(2, "Year", year)
                data_m2 = pd.read_excel(excel_file4, sheet_name= months4[(period*3)-2],  skiprows= 65, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m2.insert(1, "Period", months4[(period*3)-2])                
                data_m2.insert(2, "Year", year)
                data_m3 = pd.read_excel(excel_file4, sheet_name= months4[(period*3)-1],  skiprows= 65, nrows= 1, usecols= "G", header=None, converters={6:int})
                data_m3.insert(1, "Period", months4[(period*3)-1])                
                data_m3.insert(2, "Year", year)
                #concat the 3 months of each period
                data_all_Q_2014 = pd.concat([data_m1, data_m2, data_m3])
        
        #concat each year's same period into one dataframe
        if period==1:
            data_all_Q1 = pd.concat([data_all_Q_2011, data_all_Q_2012, data_all_Q_2013, data_all_Q_2014])
            data_all_Q1.insert(3, "Period Name", 'Ιανουαριος-Μαρτιος' )
        elif period==2:
            data_all_Q2 = pd.concat([data_all_Q_2011, data_all_Q_2012, data_all_Q_2013, data_all_Q_2014])
            data_all_Q2.insert(3, "Period Name", 'Απριλιος-Ιουνιος' )
        elif period==3:
            data_all_Q3 = pd.concat([data_all_Q_2011, data_all_Q_2012, data_all_Q_2013, data_all_Q_2014])
            data_all_Q3.insert(3, "Period Name", 'Ιουλιος-Σεπτεμβριος' )
        elif period==4:
            data_all_Q4 = pd.concat([data_all_Q_2011, data_all_Q_2012, data_all_Q_2013, data_all_Q_2014])
            data_all_Q4.insert(3, "Period Name", 'Οκτωβριος-Δεκεμβριος' )


    #uniting the dataframes into one
    data_all = pd.concat([data_all_Q1, data_all_Q2, data_all_Q3, data_all_Q4])
    data_all.columns = ['tourists', 'months', 'years', 'periods']
    #insert dataframe to table
    data_all.to_sql(name = 'periodsum', con = engine, if_exists = 'append', index = False)
    #changing the dataframe for the graph
    sum_data = pd.pivot_table(data_all, index= ['years'], columns= 'periods', values='tourists', aggfunc={'tourists': np.sum})    #creating bar graph and changing its properties
    graph = plt.figure()
    plt.ticklabel_format(style = 'plain')
    plt.title('Number of Tourists Per 3 Months Yearly')
    sum_data.plot(kind='bar', ax=graph.gca())
    plt.show()