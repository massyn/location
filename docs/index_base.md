# LocationDB - Global Location Database

LocationDB is a comprehensive, open-source geospatial database providing hierarchical location data with precise coordinates for applications requiring geographic lookup services.

Our database offers structured location information from continent level down to suburbs, making it ideal for geocoding, reverse geocoding, and location-based applications.

## Key Features

- **Hierarchical Structure**: Organized by continent → region → country → administrative divisions → cities → suburbs
- **Precise Coordinates**: Latitude and longitude data for accurate positioning
- **Comprehensive Coverage**: Global dataset with detailed location information
- **RESTful API**: Easy integration with paginated JSON responses
- **Open Source**: Free to use and community-driven development
- **Unique Identifiers**: Persistent UUIDs for stable referencing

## Quick Start

### Using the Python Client

The recommended way to access LocationDB is through our Python client library:

```python
from location import locationdb

# Initialize the client
db = locationdb()

# Download all location data
all_locations = db.download(all_pages=True)

# Get just the first page (100 records)
first_page = db.download(all_pages=False)

# Get pagination information
page_info = db.get_page_info()
print(f"Total records: {page_info['total']}")
```

### Direct API Access

You can also access the data directly via our REST API:

```python
import requests

response = requests.get('https://location-db.pages.dev/data.json')
data = response.json()

print(f"Retrieved {data['records']} of {data['total']} records")
```

For complete API documentation, see our [API Reference](api.md).

## Use Cases

- **Geocoding Services**: Convert addresses to coordinates
- **Location Validation**: Verify and standardize location data
- **Geographic Applications**: Build location-aware software
- **Data Analysis**: Spatial analysis and geographic research
- **Mobile Applications**: Location-based features and services

## Contributing

LocationDB is community-driven and welcomes contributions. Whether you're adding new locations, improving existing data, or enhancing the codebase, your contributions help make this resource better for everyone.

See our [Contribution Guide](contribute.md) for detailed instructions on how to get involved.

## Data Quality & Coverage
