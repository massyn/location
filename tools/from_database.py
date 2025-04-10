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
                        'continent' : data.get('continent',safe_get(hierarchy, 0)),
                        'region'    : data.get('region'   ,safe_get(hierarchy, 1)),
                        'country'   : data.get('country'  ,safe_get(hierarchy, 2)),
                        'admin1'    : data.get('admin1'   ,safe_get(hierarchy, 3)),
                        'admin2'    : data.get('admin2'   ,safe_get(hierarchy, 4)),
                        'city'      : data.get('city'     ,safe_get(hierarchy, 5)),
                        'suburb'    : data.get('suburb'   ,safe_get(hierarchy, 6)),
                        'latitude'  : data.get('latitude', ''),
                        'longitude' : data.get('longitude', ''),
                        'postcode'  : data.get('postcode', '')
                    })

    return output

if __name__ == '__main__':
    data = read_database('../database')
    URL = 'https://location-db.pages.dev'

    with open('../docs/index.md','at',encoding='utf-8') as md:
        md.write('## Data links\n\n')

        md.write(f"> Total of {len(data)} records found\n")

        md.write(f"* `json` - [{URL}/data.json]({URL}/data.json)\n")
        with open('../docs/data.json','wt',encoding='utf-8') as q:
            q.write(json.dumps(data))

        md.write(f"* `jsonl` - [{URL}/data.json]({URL}/data.jsonl)\n")
        with open('../docs/data.jsonl','wt',encoding='utf-8') as q:
            for i in data:
                q.write(json.dumps(i))
                q.write('\n')
