import os
import yaml
import json

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
    errors = []
    # == traverse throught the database, and get all the yaml files
    # == Create the data schema for the record
    output = []
    ids = {}
    for r, d, f in os.walk(path):
        for f2 in f:
            file = os.path.join(r, f2).replace('\\','/')[len(path)+1:]
            if file.endswith('.yaml'):
                hierarchy = file.split('.')[0].split('/')
                #print(f"Reading {file}...")
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

                        # == check if the ids are unique
                        if data['id'] in ids:
                            errors.append(f"Duplicate id detected - {file} is using an id from {ids[data['id']]}")
                        else:
                            ids[data['id']] = file

                    else:
                        errors.append(f"Missing id - {file}")

    if len(errors) == 0:
        print(f"id validation passed for {len(output)} records")
    else:
        for i in errors:
            print(f"ERROR : {i}")
        print("")
        print("** Fix these errors first before you continue **")
        exit(1)
    return output

if __name__ == '__main__':
    data = read_database('../database')
    URL = 'https://location-db.pages.dev'

    with open('../docs/index_base.md','rt',encoding='utf-8') as orig:
        with open('../docs/index.md','wt',encoding='utf-8') as md:
            for l in orig.readlines():
                md.write(f"{l}")

            md.write(f"> Total of {len(data)} records in the data set.\n\n")

            # Pagination configuration
            page_size = 100
            total_records = len(data)
            total_pages = (total_records + page_size - 1) // page_size  # Ceiling division
            
            # Generate paginated files
            for page in range(total_pages):
                start_idx = page * page_size
                end_idx = min((page + 1) * page_size, total_records)
                page_data = data[start_idx:end_idx]
                
                # Determine next page URL
                next_page = None
                if page + 1 < total_pages:
                    if page + 1 == 1:
                        next_page = f"{URL}/data1.json"
                    else:
                        next_page = f"{URL}/data{page + 1}.json"
                
                # Generate filename
                if page == 0:
                    filename = '../docs/data.json'
                else:
                    filename = f'../docs/data{page}.json'
                
                # Write paginated file
                with open(filename, 'wt', encoding='utf-8') as q:
                    q.write(json.dumps({
                        "data": page_data,
                        "next_page": next_page,
                        "records": len(page_data),
                        "total": total_records,
                        "page": page,
                        "total_pages": total_pages
                    }))

            # Calculate total size of all paginated files
            total_size = 0
            for page in range(total_pages):
                if page == 0:
                    filename = '../docs/data.json'
                else:
                    filename = f'../docs/data{page}.json'
                total_size += os.path.getsize(filename)
            
            md.write(f"The data is paginated with {page_size} records per page across {total_pages} pages.\n\n")
            md.write(f"| Format  | Link | Size |\n")
            md.write(f"|---------|------|------|\n")
            md.write(f"| `json`  | [{URL}/data.json]({URL}/data.json)   | {get_human_readable_size(total_size)}  |\n")
