# Contribute to the database

Each location is a `yaml` file, stored in a hierarchy of locations in [Github](https://github.com/massyn/location).

## How to add a new location

Create a `yaml` file with the name of the location, using the following template:

```yaml
id:
latitude: 
longitude:
postcode:
```

## Data schema

| Field       | Description                                                                                    |
|-------------|------------------------------------------------------------------------------------------------|
| `id`        | Each entry must have a unique id.  You can generate one [here](https://www.uuidgenerator.net/) |
| `latitude`  | Latitude (decimal) of the location                                                             |
| `longitude` | Longitude (decimal) of the location                                                            |
| `postcode`  | Postal code for the location                                                                   |

## About the hierarchy

The folder structure is defines as

| Column Name  | Description                                                          |
|--------------|----------------------------------------------------------------------|
| continent    | One of the seven continents (e.g., Asia, Europe, Africa)             |
| region       | Sub-continental grouping (e.g., Southeast Asia, Western Europe)      |
| country      | ISO 3166 country name (e.g., Australia, United States)               |
| admin1       | First-level admin division (e.g., state, province, canton)           |
| admin2       | Second-level division (e.g., county, district)                       |
| city         | Named populated place (city, town, or locality)                      |
| suburb       | Smaller division within a city (e.g., suburb, village, neighborhood) |

## Submit a pull request

Submit a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) to submit your contribution to the main repo.