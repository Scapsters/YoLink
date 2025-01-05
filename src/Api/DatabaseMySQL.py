import json
import mysql.connector
from Interfaces.Database import Database
from collections import OrderedDict
from datetime import  *
import mysql

from Interfaces.Data.Event import Event
from Interfaces.Device import Device
from Interfaces.Credentials.MySQLCredentials import MySQLCredentials

class DatabaseMySQL(Database):
    
    def __init__(self, current_user):
        
        # TODO: rename parent folder to db or something
        
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
        
        self.reset() # TODO: remove this at some point
        self.setup()
    
    def setup(self):
        self.execute_file("./../my_sql/sql/setup.sql", { "schema_name": self.credentials.database_name })
    
    def reset(self):
        self.execute_file("./../my_sql/sql/reset.sql", { "schema_name": self.credentials.database_name })
      
    def add_event_and_entries(self, event: Event) -> None:
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO events
                (event_source_device_id, event_timestamp) 
                VALUES (%(source_device_id)s, %(timestamp)s)
        """, {
            "source_device_id": event.source_device_id,
            "timestamp": event.timestamp
        })
        event_id = cursor.lastrowid # i dont like mysql anymore
        
        for data_entry in event.data_entries:
            cursor.execute("""
                INSERT INTO data
                    (event_id, data_name, data_value)
                    VALUES (%(event_id)s, %(name)s, %(value)s)
            """, {
                "event_id": event_id,
                "name": data_entry.name,
                "value": data_entry.value
            })
        self.connection.commit()
        
    def save(self):
        pass
    
    def add_device(self, device: Device):
        cursor = self.connection.cursor()
        cursor.execute("""
            INSERT INTO devices
                (device_id, device_type, device_name, device_token, device_timestamp)
                VALUES (%(device_id)s, %(device_type)s, %(device_name)s, %(device_token)s, %(device_timestamp)s)
        """, {
            "device_id": device.device_id,
            "device_name": device.name,
            "device_type": device.type,
            "device_token": device.token,
            "device_timestamp": datetime.now()
        })
        self.connection.commit()
    
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
        self.connection.commit()
                
        
        
