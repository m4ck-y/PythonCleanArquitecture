import json
import os

def read_json(nameFileDB, defaultValue={})->object:
    if not os.path.isfile(nameFileDB):
        write_json(nameFileDB, defaultValue)

    with open(nameFileDB, "r") as f:
        data = json.load(f)
    return data
    
def write_json(nameFileDB, data:object):
    with open(nameFileDB, "w") as f:
        print("JSON:", json.dumps(data))
        json.dump(data, f)