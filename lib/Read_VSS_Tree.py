import json
import os

path_dict = dict()
path = []

def check_child(data):
    if(len(data.keys()) == 0):
        path.pop()
    for key, val in data.items():
        if(val["type"] == "branch"):
            path.append(key+".")
            check_child(val["children"])
        else:
            path.append(key)
            path_dict["".join(path)] = val
            print("".join(path))
            path.pop()
            print("==================")

# Opening JSON file
f = open('../Demo_VSS_tree/new_signal.json')
#f = open('../Demo_VSS_tree/steering_switch_signal.json')
  
# Reading from file
data = json.loads(f.read())
check_child(data)
for key, val in path_dict.items():
    print(key+":")
    for line in val.items():
        print(line)
# Closing file
f.close()