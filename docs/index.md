# Location Database

The location database is a community driven, open source location database that can be used in applications that require some sort of GPS-to-location lookup service.

The data is free and open to anyone.  It may not be fully accurate, and that's where you come in.  If you find a location is missing, you're welcome to contibute, and add your location to the database.

## How to use the API

The database is presented in a number of formats.  The simplest way is to simply read the `json` file and use it in your application.

```python
import requests

data = requests.get('https://location-db.pages.dev/data.json').json()
```
## How to contribute

The database is all in [Github](https://github.com/massyn/location).  Like all github projects, you're invited to make updates, and submit a pull request to have your updates applied.  Refer to the [contribute](contribute.md) page for more information.

## Data files

The data files are produced in a number of different formats.  Pick the one that matches your requirements the closest.

