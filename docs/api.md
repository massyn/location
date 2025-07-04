# LocationDB API Reference

## Overview

The LocationDB API provides programmatic access to our comprehensive geospatial database. Access structured location data with precise coordinates organized in a hierarchical format from continent level down to suburbs.

**Current API Version**: v1  
**Response Format**: JSON  
**Rate Limiting**: None (subject to fair use)

## Base URL
```
https://location-db.pages.dev/
```

## Endpoints

### Get Location Data
```
GET /data.json
GET /data1.json
GET /data2.json
...
```

Retrieves a paginated set of location records. The first page is available at `/data.json`, with subsequent pages at `/data1.json`, `/data2.json`, etc.

#### Response Format

The response is a JSON object with the following structure:

```json
{
  "data": [
    {
      "id": "string",
      "continent": "string",
      "region": "string", 
      "country": "string",
      "admin1": "string",
      "admin2": "string",
      "city": "string",
      "suburb": "string",
      "latitude": "number",
      "longitude": "number",
      "postcode": "string"
    },
    ...
  ],
  "next_page": "string | null",
  "records": "number",
  "total": "number",
  "page": "number",
  "total_pages": "number"
}
```

#### Response Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | array | List of location records (maximum 100 per page) |
| `next_page` | string or null | URL to call to retrieve the next page of results. If `null`, there are no more pages available |
| `records` | number | Count of records in the current response |
| `total` | number | Total number of records in the entire dataset |
| `page` | number | Current page number (0-indexed) |
| `total_pages` | number | Total number of pages in the dataset |

#### Location Record Schema

Each location record in the `data` array contains the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique identifier (GUID) for the location |
| `continent` | string | Name of the continent |
| `region` | string | Regional designation |
| `country` | string | Country name |
| `admin1` | string | First-level administrative division (e.g., state, province) |
| `admin2` | string | Second-level administrative division (e.g., county, district) |
| `city` | string | City name |
| `suburb` | string | Suburb or neighborhood name |
| `latitude` | number | Geographic latitude coordinate |
| `longitude` | number | Geographic longitude coordinate |
| `postcode` | string | Postal or ZIP code |

## Pagination

The API uses page-based pagination with 100 records per page. Each page contains metadata about the total dataset and navigation information. To retrieve all data:

1. Make an initial request to `/data.json` (page 0)
2. Check if the `next_page` field is not `null`
3. If available, make a follow-up request to the URL specified in `next_page`
4. Repeat steps 2-3 until `next_page` is `null`

### Page Numbering
- Page 0: `/data.json` (first page)
- Page 1: `/data1.json` 
- Page 2: `/data2.json`
- Page N: `/dataN.json`

## Example Usage

### Python Example

```python
import requests
import json

def fetch_all_location_data():
    all_data = []
    next_url = "https://location-db.pages.dev/data.json"
    
    while next_url:
        # Make the API request
        response = requests.get(next_url)
        response_data = response.json()
        
        # Add this page's data to our collection
        all_data.extend(response_data["data"])
        
        # Prepare for next page if available
        next_url = response_data["next_page"]
        
        # Output progress
        print(f"Fetched page {response_data['page']}: {len(response_data['data'])} records. " 
              f"Progress: {len(all_data)}/{response_data['total']} "
              f"({response_data['page'] + 1}/{response_data['total_pages']} pages)")
    
    return all_data

# Retrieve all location data
locations = fetch_all_location_data()
print(f"Retrieved {len(locations)} locations in total")

# Alternative: Use the location.py library
from location import locationdb

location_db = locationdb()
# Download all pages
all_locations = location_db.download(all_pages=True)
# Or download just first page
first_page = location_db.download(all_pages=False)
```

## Error Handling

The API uses standard HTTP status codes to indicate success or failure:

| Status Code | Description |
|-------------|-------------|
| `200 OK` | Request succeeded |
| `404 Not Found` | Requested page does not exist |
| `429 Too Many Requests` | Rate limit exceeded (if applicable) |
| `500 Internal Server Error` | Server error occurred |
| `503 Service Unavailable` | Service temporarily unavailable |

### Error Response Format

When an error occurs, the API returns a JSON response with error details:

```json
{
  "error": {
    "code": "NOT_FOUND",
    "message": "The requested page does not exist",
    "details": "Page data15.json not found"
  }
}
```

## Best Practices

### Performance Optimization
- Cache responses locally when possible
- Use pagination efficiently - only fetch pages you need
- Implement exponential backoff for retry logic

### Data Handling
- Always validate location data before use
- Handle missing or null fields gracefully  
- Consider data freshness for your use case

### Integration Guidelines
- Use the Python client library for simplified integration
- Implement proper error handling for network failures
- Monitor API responses for changes in data structure

## Rate Limiting

Currently, there are no enforced rate limits, but please use the API responsibly:
- Avoid excessive concurrent requests
- Cache data locally to reduce API calls
- Use bulk operations (download all pages) when appropriate
- Contact us for high-volume usage requirements

## Support

For API support, bug reports, or feature requests:
- GitHub Issues: [https://github.com/massyn/location/issues](https://github.com/massyn/location/issues)
- Documentation: [https://location-db.pages.dev](https://location-db.pages.dev)