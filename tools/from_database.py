import os
import yaml
import json

def safe_get(lst, index, default=''):
    try:
        return lst[index]
    except IndexError:
        return default
    
def read_database(path):
    # == traverse throught the database, and get all the yaml files
    # == Create the data schema for the record
    output = []
    for r, d, f in os.walk(path):
        for f2 in f:
            file = os.path.join(r, f2).replace('\\','/')[len(path)+1:]
            if file.endswith('.yaml'):
                hierarchy = file.split('.')[0].split('/')
                print(f"Reading {file}...")
                with open(f"{path}/{file}",'rt',encoding='utf-8') as y:
                    data = yaml.safe_load(y)
                    output.append({
                        'continent' : safe_get(hierarchy, 0),
                        'region'    : safe_get(hierarchy, 1),
                        'country'   : safe_get(hierarchy, 2),
                        'admin1'    : safe_get(hierarchy, 3),
                        'admin2'    : safe_get(hierarchy, 4),
                        'city'      : safe_get(hierarchy, 5),
                        'suburb'    : safe_get(hierarchy, 6),
                        'lattitude' : data.get('lattitude', ''),
                        'longitude' : data.get('longitude', ''),
                        'postcode'  : data.get('postcode', '')
                    })

    return output

if __name__ == '__main__':
    data = read_database('../database')

    with open('docs/data.json','wt',encoding='utf-8') as q:
        q.write(json.dumps(data))

    with open('docs/data.jsonl','wt',encoding='utf-8') as q:
    for i in data:
        q.write(json.dumps(i))
        q.write('\n')
