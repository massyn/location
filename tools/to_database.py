import requests
from dotenv import load_dotenv
import os
import io
import csv
import uuid

def main(target):
    x = os.environ['GOOGLE_SHEET']
    req = requests.get(x)
    dryrun = False

    if req.status_code == 200:
        decoded = req.content.decode('utf-8')
        reader = csv.DictReader(io.StringIO(decoded))
        for row in reader:
            # -- produce the file path
            file_bits = []
            for i in ['continent','region','country','admin1','admin2','city','suburb']:
                file_bits.append(row[i]) if row[i] != '' else None
            
            file = f"{target}/{'/'.join(file_bits)}.yaml"
            
            if not os.path.exists(file):
                if dryrun:
                    print(f"Will write {file}")
                    print(f"id: {str(uuid.uuid4())}\n")
                    print(f"latitude: {row['latitude']}\n")
                    print(f"longitude: {row['longitude']}\n")
                    print(f"postcode: \"{row['postcode']}\"\n")
                else:
                    print(f"Writing {file}...")
                    os.makedirs(os.path.dirname(file), exist_ok=True)
                    with open(file,'wt',encoding='utf-8') as q:
                        q.write(f"id: {str(uuid.uuid4())}\n")
                        q.write(f"latitude: {row['latitude']}\n")
                        q.write(f"longitude: {row['longitude']}\n")
                        q.write(f"postcode: \"{row['postcode']}\"\n")
                    
                    os.system(f"git add \"{file}\"")
    else:
        print(f"Something went wrong = {req.status_code}")
        print(req.content)


if __name__ == '__main__':
    load_dotenv()
    main('../database')