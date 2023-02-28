import pyodbc
import pandas as pd
import connect as c

conn = pyodbc.connect(c.connect())

def storeName():
    Name = []
    query = 'select Name from sites'
    print(conn,'\n',query)
    data = pd.read_sql(query,conn)
    return data
    
def storeCode():
    query = 'select siteid from sites'
    print(conn,'\n',query)
    data = pd.read_sql(query,conn)
    return data
def ipAddress():
    query = 'select Description from sites'
    print(conn,'\n',query)
    data = pd.read_sql(query,conn)
    return data

def groupTable():
    query = '''
    select 
    Name,
    st.siteid,
    loc.description,
    'MAC' as 'MAC Address'
    from sites st 
    full join location loc on st.siteid = loc.siteid
    group by st.siteid,Name,loc.description
    '''
    print(conn,'\n',query)
    data = pd.read_sql(query,conn)
    return data