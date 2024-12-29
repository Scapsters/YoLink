import json
import mysql.connector
from Interfaces.Database import Database
from collections import OrderedDict
import mysql

from Interfaces.Credentials.MySQLCredentials import MySQLCredentials

class DatabaseMySQL(Database):
    
    def __init__(self, current_user):
        
        # TODO: should these credential details be kept as class attributes?
        # This would allow for recreation of a connection without needing to reread the file.
        # But maybe its a security issue?
        
        # Extract credentials as attributes
        with open("./../credentials.json", "r") as file:
            credentials_json = json.load(file)
        
        self.credentials = MySQLCredentials(
            database_name = credentials_json[current_user + "_mysql_database_name"],
            host          = credentials_json[current_user + "_mysql_host"],
            port          = credentials_json[current_user + "_mysql_port"],
            username      = credentials_json[current_user + "_mysql_username"],
            password      = credentials_json[current_user + "_mysql_password"]
        )
        
        # Create connection
        self.connection = self.create_connection()
        
        # Test connection
        self.connection.ping()
        
        self.reset() # TODO: remove this at some point
        self.setup()
    
    def setup(self):
        self.execute_file("./../my_sql/sql/setup.sql", { "schema_name": self.credentials.database_name })
    
    def reset(self):
        self.execute_file("./../my_sql/sql/reset.sql", { "schema_name": self.credentials.database_name })
      
    def save(self, device_type: str, header: OrderedDict[str, str|int]) -> None:
        cursor = self.connection.cursor()
        
    def add_device(self, device_id, device_name, device_type, timestamp):
        return super().add_device(device_id, device_name, device_type, timestamp)
    
    def create_connection(self):
        return mysql.connector.connect(
            database = self.credentials.database_name,
            host     = self.credentials.host,
            port     = self.credentials.port,
            username = self.credentials.username,
            password = self.credentials.password,
        )
        
    def execute_file(self, filename, params):
        with open(filename, 'r') as sql_file:
            sql = sql_file.read()
            sql = sql % params
            sql_statements = sql.split(";")
            
            for statement in sql_statements:
                print('executing: ' + statement)
                print(params)
                self.connection.cursor().execute(statement)
                
        
        
