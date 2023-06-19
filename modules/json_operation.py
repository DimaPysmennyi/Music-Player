import json
import modules.find_path as m_path
import modules.data as m_data

def write_json():
    with open(m_path.find_path("json\\data.json"), "w") as file:
        json.dump(m_data.data, file, indent = 4)

def read_json():
    with open(m_path.find_path("json\\data.json"), "r") as file:
        info = json.load(file)
        return info
    
m_data.data = read_json()
print(m_data.data)