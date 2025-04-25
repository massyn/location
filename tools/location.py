import requests

class locationdb:
    def __init__(self):
        self.endpoint = "https://location-db.pages.dev/"

    # in future, this method will be updated and become paginated.  Where possible, use this class to retrieve the data.
    def download(self):
        req = requests.get(f"{self.endpoint}/data.json",timeout=30)
        req.raise_for_status()
        if req.status_code == 200:
            return req.json()
        else:
            return []
        
if __name__ == '__main__':
    location = locationdb()

    for x in location.download():
        print(x)
