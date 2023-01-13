from importlib.resources import path
import json
import sys
import utils


class JSONFile:

    def __init__(self, f_dir):
        self.f_dir  = f_dir
        

    def read(self, f_name: str) -> dict:
        data = {}
        
        if not isinstance(f_name, str):
            raise TypeError("path not str type.")
        
        temp = f_name.split(".")
        if temp[-1] != "json":  # gets last element split by "."
            raise ValueError("File not json type.")
        
        f_path = utils.set_path(file_name=f_name, file_dir=self.f_dir)
    
        try:
            with open(f_path, "r") as f:
                data = json.load(f)
        
        except FileNotFoundError:
            print(sys.exc_info()[0])
            
        except json.decoder.JSONDecodeError:
            print(sys.exc_info()[0])
                
        return data


    def write(self, f_name: str, data: dict):
        if not isinstance(f_name, str):
            raise TypeError("path not str type.")
        
        if not isinstance(data, dict):
            raise TypeError("data not dict type.")
        
        temp = f_name.split(".")
        if temp[-1] != "json":  # gets last element split by "."
            raise ValueError("File not json type.")
        
        f_path = utils.set_path(file_name=f_name, file_dir=self.f_dir)
        
        with open(f_path, "w") as f:
            json.dump(data, f, indent=4)