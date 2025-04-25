# Location Data API

## Overview
This API provides access to a comprehensive database of location data including geographical coordinates and hierarchical location information from continent down to suburb level.

## Base URL
```
https://location-db.pages.dev/
```

## Endpoints

### Get Location Data
```
GET /data.json
```

Retrieves a paginated set of location records.

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
  "total": "number"
}
```

#### Response Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `data` | array | List of location records |
| `next_page` | string or null | URL to call to retrieve the next page of results. If `null`, there are no more pages available |
| `records` | number | Count of records in the current response |
| `total` | number | Total number of records in the entire dataset |

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

The API uses cursor-based pagination through the `next_page` field in the response. To retrieve all data:

1. Make an initial request to `/data.json`
2. Check if the `next_page` field is not `null`
3. If available, make a follow-up request to the URL specified in `next_page`
4. Repeat steps 2-3 until `next_page` is `null`

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
        print(f"Fetched {len(response_data['data'])} records. " 
              f"Progress: {len(all_data)}/{response_data['total']}")
    
    return all_data

# Retrieve all location data
locations = fetch_all_location_data()
print(f"Retrieved {len(locations)} locations in total")
```

## Error Handling

The API does not define specific error responses. Standard HTTP status codes apply:

- `200 OK`: Request succeeded
- `404 Not Found`: Resource not found
- `5xx`: Server error

## Rate Limiting

This documentation does not specify rate limiting details. Implement reasonable request throttling in production applications.