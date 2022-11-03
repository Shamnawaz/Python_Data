import mysql.connector
import pandas as pd




def db_connect():
    # https://phpmyadmin.alwaysdata.com/
    mydb = mysql.connector.connect(
        host="mysql-ali-ipssi.alwaysdata.net",
        user="ali-ipssi",
        password="Ipssi2020",
        database="ali-ipssi_aeroport"
    ) 
    return mydb
