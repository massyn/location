# Using the API

The database is presented in a number of formats.  The simplest way is to simply read the `json` file and use it in your application.

```python
import requests

data = requests.get('https://location-db.pages.dev/data.json').json()
```

## How to use the data

When linking the data with your own data set, join the data on the `id` column.  This column should not change.

