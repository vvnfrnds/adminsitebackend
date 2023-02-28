import pyodbc
import pandas as pd
import connect as c

conn = pyodbc.connect(c.connect())

def bodyView():
    query = ''' 
    select 
    Name,
    st.siteid,
    unitID,
    cameraId,
    loc.description,
    'MAC' as 'MAC Address'
    from sites st 
    full join location loc on st.siteid = loc.siteid
    group by st.siteid,Name,unitID,cameraId,
    loc.description
    '''
    data = pd.read_sql(query,conn)
    return data