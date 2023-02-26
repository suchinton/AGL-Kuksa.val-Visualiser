import json
  
def check_child(**input):
    if(input["children"]):
        check_child(input["children"])
    else:
        print(input["children"])


# Opening JSON file
f = open('steering_switch_signal.json')
  
# Reading from file
data = json.loads(f.read())
data = dict(data)
print(type(data))

#check_child(data)
  
# Closing file
f.close()