from pydantic.dataclasses import dataclass

@dataclass
class MySQLCredentials:
    database_name: str
    host: str | int #TODO: I dont really know if they can be either but assuming theyre really just sent to MySQL its fine
    port: str | int
    username: str
    password: str