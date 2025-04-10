import os
import yaml
import json
import csv

def writeCSV(file,data):
    os.makedirs(os.path.dirname(file),exist_ok = True)
    headers = list(data[0])
    with open(file, 'wt', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)

        for x in data:
            row = []
            for h in headers:
                row.append(x.get(h))
            csvwriter.writerow(row)

def safe_get(lst, index, default=''):
    try:
        return lst[index]
    except IndexError:
        return default

def get_human_readable_size(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"
    elif size_in_bytes < 1024**2:
        return f"{size_in_bytes / 1024:.2f} KB"
    elif size_in_bytes < 1024**3:
        return f"{size_in_bytes / 1024**2:.2f} MB"
    else:
        return f"{size_in_bytes / 1024**3:.2f} GB"
        
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
                    if 'id' in data:
                        output.append({
                            'id'        : data.get('id'),
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
                    else:
                        print(f"ERROR : {file} is missing id")

    return output

if __name__ == '__main__':
    data = read_database('../database')
    URL = 'https://location-db.pages.dev'

    with open('../docs/index.md','at',encoding='utf-8') as md:
        md.write('## Data links\n\n')

        md.write(f"> Total of {len(data)} records found\n\n")

        with open('../docs/data.json','wt',encoding='utf-8') as q:
            q.write(json.dumps(data))

        with open('../docs/data.jsonl','wt',encoding='utf-8') as q:
            for i in data:
                q.write(json.dumps(i))
                q.write('\n')
        writeCSV('../docs/data.csv',data)

        md.write(f"| Format  | Link | Size |\n")
        md.write(f"|---------|------|------|\n")
        md.write(f"| `json`  | [{URL}/data.json]({URL}/data.json)  | {get_human_readable_size(os.path.getsize('../docs/data.json'))}  |\n")
        md.write(f"* `jsonl` | [{URL}/data.json]({URL}/data.jsonl) | {get_human_readable_size(os.path.getsize('../docs/data.jsonl'))} |\n")
        md.write(f"* `csv`   | [{URL}/data.json]({URL}/data.json)  | {get_human_readable_size(os.path.getsize('../docs/data.json'))}  |\n")
