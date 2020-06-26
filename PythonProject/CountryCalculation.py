import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import pymysql
from sqlalchemy import create_engine


#saws the amount of tourists yearly in Greece from 2011 - 2015
def country_sum():
    
    #establishing mysql connection with two different ways
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="xxxx",
    auth_plugin='mysql_native_password',
    database="PythonProject"
    )
    #creating engine for mysql connection in order to use pandas.to_sql() function
    engine = create_engine('mysql+pymysql://root:pao134ever@localhost:3306/PythonProject', echo = False)
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS PythonProject")

    #doing the same process for every year 
    for year in range(2011, 2015):
        period = 4
        #creating the correct filename
        name_id =str(year) + "-Q" + str(period)
        if year==2011:    
            excel_file1 = name_id + '.xls'     
            #reading the right rows from the last sheet of the excels and editing the dataframe form
            data1 = pd.read_excel(excel_file1, sheet_name= 'ΔΕΚ',  skiprows= 76, nrows= 58, usecols= "B,G", header=None, converters={6:int})
            data1.insert(2, "Year", year)
            data1.columns = ['country', 'tourists', 'years']
            data1[data1.country != 'NaN']
            #create the table that data will be stored
            mycursor.execute("DROP TABLE IF EXISTS countrysum2011")
            mycursor.execute("CREATE TABLE IF NOT EXISTS countrysum2011(iD INT AUTO_INCREMENT, country VARCHAR(255), tourists BIGINT, years INT, PRIMARY KEY(iD,years))")
            #insert dataframe to table
            data1.to_sql(name = 'countrysum2011', con = engine, if_exists = 'append', index = False)

        if year==2012:    
            excel_file2 = name_id + '.xls'     
            #reading the right rows from the last sheet of the excels and editing the dataframe form
            data2 = pd.read_excel(excel_file2, sheet_name= 'ΔΕΚ',  skiprows= 78, nrows= 58, usecols= "B,G", header=None, converters={6:int})
            data2.insert(2, "Year", year)
            data2.columns = ['country', 'tourists', 'years']
            data2[data2.country != 'NaN']
            mycursor.execute("DROP TABLE IF EXISTS countrysum2012")
            mycursor.execute("CREATE TABLE IF NOT EXISTS countrysum2012(iD INT AUTO_INCREMENT, country VARCHAR(255), tourists BIGINT, years INT, PRIMARY KEY(iD,years))")
            #insert dataframe to table
            data2.to_sql(name = 'countrysum2012', con = engine, if_exists = 'append', index = False)

        if year==2013:    
            excel_file3 = name_id + '.xls'     
            #reading the right rows from the last sheet of the excels and editing the dataframe form
            data3 = pd.read_excel(excel_file3, sheet_name= 'ΔΕΚ',  skiprows= 78, nrows= 58, usecols= "B,G", header=None, converters={6:int})
            data3.insert(2, "Year", year)
            data3.columns = ['country', 'tourists', 'years']
            data3[data3.country != 'NaN']
            mycursor.execute("DROP TABLE IF EXISTS countrysum2013")
            mycursor.execute("CREATE TABLE IF NOT EXISTS countrysum2013(iD INT AUTO_INCREMENT, country VARCHAR(255), tourists BIGINT, years INT, PRIMARY KEY(iD,years))")
            #insert dataframe to table
            data3.to_sql(name = 'countrysum2013', con = engine, if_exists = 'append', index = False)

        if year==2014:    
            excel_file4 = name_id + '.xls'     
            #reading the right rows from the last sheet of the excels and editing the dataframe form
            data4 = pd.read_excel(excel_file4, sheet_name= 'ΔΕΚ',  skiprows= 78, nrows= 58, usecols= "B,G", header=None, converters={6:int})
            data4.insert(2, "Year", year)
            data4.columns = ['country', 'tourists', 'years']
            data4[data4.country != 'NaN']
            mycursor.execute("DROP TABLE IF EXISTS countrysum2014")
            mycursor.execute("CREATE TABLE IF NOT EXISTS countrysum2014(iD INT AUTO_INCREMENT, country VARCHAR(255), tourists BIGINT, years INT, PRIMARY KEY(iD,years))")
            #insert dataframe to table
            data4.to_sql(name = 'countrysum2014', con = engine, if_exists = 'append', index = False)


    #uniting the dataframes into one
    data_all = pd.concat([data1, data2, data3, data4])
    #changing the dataframe for the graph
    sum_country_year = data_all.pivot_table(index= 'country', columns= 'years', values='tourists', aggfunc={'tourists': np.mean})
    #creating bar graph and changing its properties
    graph = plt.figure()
    plt.ticklabel_format(style = 'plain')
    plt.title('Number of Tourists per Country Yearly')
    sum_country_year.plot(kind='barh', ax=graph.gca())
    plt.show()