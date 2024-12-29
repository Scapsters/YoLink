import os
from datetime import date
from collections import OrderedDict

from Interfaces.Database import Database

SAVE_DIR = 'data'
SAVE_EXT = '.csv'

class DatabaseCSV(Database):
    def save(self, device_type: str, header: OrderedDict[str, str|int]) -> None:
        
        return None
        # Create filepath
        filename = f'/{device_type}-{date.today().strftime("%m-%d-%y")}'
        filepath = SAVE_DIR + filename + SAVE_EXT

        # Regardless of whether the file exists, it will be appended to
        with open(filepath, 'a+') as file:
                    
            # If the file is empty, add headers
            if os.path.getsize(filepath) == 0:
                for header_item in header:
                    file.write(f'{header_item},')

            # Newline and enter data
            file.write('\n')
            values = header.values()
            for value in values:
                file.write(f'{value},')