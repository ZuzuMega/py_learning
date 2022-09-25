from base64 import encode
from cgitb import html
from distutils.log import error
import re
import requests
import os
import time

sql_errors = {
    "MySQL": (r"SQL syntax.*MySQL", r"Warning.*mysql_.*", r"MySQL Query fail.*", r"SQL syntax.*MariaDB server"),
    "PostgreSQL": (r"PostgreSQL.*ERROR", r"Warning.*\Wpg_.*", r"Warning.*PostgreSQL"),
    "Microsoft SQL Server": (r"OLE DB.* SQL Server", r"(\W|\A)SQL Server.*Driver", r"Warning.*odbc_.*", r"Warning.*mssql_", r"Msg \d+, Level \d+, State \d+", r"Unclosed quotation mark after the character string", r"Microsoft OLE DB Provider for ODBC Drivers"),
    "Microsoft Access": (r"Microsoft Access Driver", r"Access Database Engine", r"Microsoft JET Database Engine", r".*Syntax error.*query expression"),
    "Oracle": (r"\bORA-[0-9][0-9][0-9][0-9]", r"Oracle error", r"Warning.*oci_.*", "Microsoft OLE DB Provider for Oracle"),
    "IBM DB2": (r"CLI Driver.*DB2", r"DB2 SQL error"),
    "SQLite": (r"SQLite/JDBCDriver", r"System.Data.SQLite.SQLiteException"),
    "Informix": (r"Warning.*ibase_.*", r"com.informix.jdbc"),
    "Sybase": (r"Warning.*sybase.*", r"Sybase message")
}

# Analyze HTML code on sites
def checkSQL(html_code):
    for db, errors in sql_errors.items():
        for error in errors:
            if re.compile(error).search(html):
                return True, db
    return False, None

file_sites = open('C:/Projects/py_learning/les_3/SQL-scaner/urls.txt', 'r', encoding='UTF-8')
file_errors = open('good.txt', 'w', encoding='UTF-8')


def check(url):
    x = url.replace("&","'&")
    url = x.strip()
    if not(ur[0:4] == 'http'):
        ur = 'http://' + ur
    print ("Check a: " + ur)
    try:
        s = requests.get(ur +"'")
        h = s.text
        a, b = checkSQL(h)
        if(a):
            print("was found vuinerability for SQL scrips: " + ur)
            file_errors(f'{ur} - {str(b)}\n')
        else:
            print("a vuinerability was not find: "+ur)
    except:
        print("Erroe in check: "+ ur)
        pass

for site in file_sites:
    check(site)


file_sites.close()
file_errors.close()

