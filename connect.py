import os
from dotenv import load_dotenv
load_dotenv()

def connect():
    server = os.getenv('SERVER')
    database = os.getenv('DATABASE')
    driver = os.getenv('DRIVER')
    connectionstring = f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;1'
    # print(connectionstring)
    return connectionstring
