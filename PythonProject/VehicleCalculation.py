import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import pymysql
from sqlalchemy import create_engine


#saws the amount of tourists yearly in Greece from 2011 - 2015
def sum_by_vehicle():
    #establishing connections fro data base
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xxxx",
    auth_plugin='mysql_native_password',
    database="PythonProject"
    )
    engine = create_engine('mysql+pymysql://root:pao134ever@localhost:3306/PythonProject', echo = False)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS PythonProject")
    mycursor.execute("CREATE TABLE IF NOT EXISTS vehiclesum (TYPES TEXT, AIR BIGINT, TRAIN BIGINT, SEA BIGINT, ROAD BIGINT, years INT AUTO_INCREMENT PRIMARY KEY)")

    for year in range(2011, 2015):
        period = 4
        name_id =str(year) + "-Q" + str(period)
        if year==2011:    
            excel_file1 = name_id + '.xls'     
            #reading the right rows from the last sheet of the excels
            data1 = pd.read_excel(excel_file1, sheet_name= 'ΔΕΚ',  skiprows= 134, nrows= 1, usecols= "B,C,D,E,F", header=None, converters={2:int, 3:int, 4:int, 5:int})
            data1.insert(5, "Year", year)
        if year==2012:    
            excel_file2 = name_id + '.xls'     
            #reading the right rows from the last sheet of the excels
            data2 = pd.read_excel(excel_file2, sheet_name= 'ΔΕΚ',  skiprows= 136, nrows= 1, usecols= "B,C,D,E,F", header=None, converters={2:int, 3:int, 4:int, 5:int})
            data2.insert(5, "Year", year)
        if year==2013:    
            excel_file3 = name_id + '.xls'     
            #reading the right rows from the last sheet of the excels
            data3 = pd.read_excel(excel_file3, sheet_name= 'ΔΕΚ',  skiprows= 136, nrows= 1, usecols= "B,C,D,E,F", header=None, converters={2:int, 3:int, 4:int, 5:int})
            data3.insert(5, "Year", year)
        if year==2014:    
            excel_file4 = name_id + '.xls'     
            #reading the right rows from the last sheet of the excels
            data4 = pd.read_excel(excel_file4, sheet_name= 'ΔΕΚ',  skiprows= 136, nrows= 1, usecols= "B,C,D,E,F", header=None, converters={2:int, 3:int, 4:int, 5:int})
            data4.insert(5, "Year", year)

    #uniting the dataframes into one
    data_all = pd.concat([data1, data2, data3, data4])
    data_all.columns = ['TYPES', 'AIR', 'TRAIN', 'SEA', 'ROAD', 'YEARS']
    #make table empty
    mycursor.execute("DROP TABLE IF EXISTS vehiclesum")
    #insert dataframe to table
    data_all.to_sql(name = 'vehiclesum', con = engine, if_exists = 'append', index = False)
    #changing the dataframe for the graph
    sum_year = data_all.pivot_table(index= 'YEARS', columns= 'TYPES', values=['AIR','TRAIN','SEA','ROAD'])
    #creating bar graph and changing its properties
    graph = plt.figure()
    plt.ticklabel_format(style = 'plain')
    plt.title('Number of Tourists Yearly By Vehicle')
    sum_year.plot(kind='bar', ax=graph.gca())
    plt.show()