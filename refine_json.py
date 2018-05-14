import json
import os
import glob

root =os.getcwd()
json_path =os.path.join(root, 'json', '*.json')
json_file = glob.glob(json_path)

for filename in json_file:
    new_data = []
    with open(filename, encoding='utf-8') as f:
        data = json.load(f)
        for dit in data['shapes']:
            dit['label'] = 'damage'
        new_data = data
    with open(filename,'w') as f:
        data = json.dump(new_data,f)