import requests

class locationdb:
    def __init__(self):
        self.endpoint = "https://location-db.pages.dev/"

    def download(self, all_pages=True):
        """
        Download location data from the API.
        
        Args:
            all_pages (bool): If True, downloads all pages. If False, downloads only the first page.
        
        Returns:
            list: List of location records
        """
        if all_pages:
            return self._download_all_pages()
        else:
            return self._download_single_page(f"{self.endpoint}/data.json")
    
    def _download_single_page(self, url):
        """Download a single page of data"""
        req = requests.get(url, timeout=30)
        req.raise_for_status()
        if req.status_code == 200:
            return req.json()['data']
        else:
            return []
    
    def _download_all_pages(self):
        """Download all pages of data"""
        all_data = []
        next_url = f"{self.endpoint}/data.json"
        
        while next_url:
            req = requests.get(next_url, timeout=30)
            req.raise_for_status()
            
            if req.status_code == 200:
                response_data = req.json()
                all_data.extend(response_data['data'])
                next_url = response_data['next_page']
            else:
                break
        
        return all_data
    
    def get_page_info(self, page_url=None):
        """
        Get pagination information for a specific page.
        
        Args:
            page_url (str, optional): URL of the page to get info for. Defaults to first page.
        
        Returns:
            dict: Page information including total records, total pages, current page, etc.
        """
        if page_url is None:
            page_url = f"{self.endpoint}/data.json"
        
        req = requests.get(page_url, timeout=30)
        req.raise_for_status()
        
        if req.status_code == 200:
            response_data = req.json()
            return {
                'total': response_data['total'],
                'total_pages': response_data['total_pages'],
                'current_page': response_data['page'],
                'records_in_page': response_data['records'],
                'next_page': response_data['next_page']
            }
        else:
            return {}
        
if __name__ == '__main__':
    location = locationdb()

    # Example: Download all data
    print("Downloading all pages...")
    all_data = location.download(all_pages=True)
    print(f"Downloaded {len(all_data)} total records")
    
    # Example: Download only first page
    print("\nDownloading first page only...")
    first_page = location.download(all_pages=False)
    print(f"Downloaded {len(first_page)} records from first page")
    
    # Example: Get page info
    page_info = location.get_page_info()
    print(f"\nPage info: {page_info}")
    
    # Print first few records
    print("\nFirst 3 records:")
    for i, record in enumerate(first_page[:3]):
        print(f"  {i+1}: {record}")
