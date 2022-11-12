import json
import os
import yaml

os.getcwd()

# Ex_1
with open("user.json") as json_file:
    data = json.load(json_file)

with open("text.txt", "w") as text_file:
    json.dump(data, text_file, indent=3)

# Ex_2
with open("user.json") as js:
    js_data = json.load(js)

with open("yaml_file.yaml", "w") as yml:
    yaml.dump(js_data, yml)

# Ex_3
with open("yaml_file.yaml") as yf:
    data = yaml.safe_load(yf)

with open("user.json", "w") as js_file:
    json.dump(data, js_file, indent=3)

# Ex_4
with open("yaml_file.yaml") as y_file:
    data = yaml.safe_load(y_file)

with open("text.txt", "w") as text_read:
    yaml.dump(data, text_read, indent=4)
