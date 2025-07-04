# Location Finder

Use this interactive tool to find your current location in the LocationDB database. The tool uses your browser's GPS capabilities to determine your coordinates and then searches for the closest matching location in our database.

## How it Works

1. **GPS Access**: Your browser will request permission to access your location
2. **Coordinate Detection**: We capture your current latitude and longitude
3. **Database Search**: The tool searches LocationDB for the nearest location
4. **Results Display**: Shows the closest match with distance information

## Privacy Notice

- Location data is processed locally in your browser
- No location information is stored or transmitted to our servers
- GPS access requires your explicit permission

<iframe src="../assets/find.html" width="600" height="450" frameborder="1" marginheight="0" marginwidth="0" title="Location Finder Tool"></iframe>

## Accuracy Notes

- Results depend on GPS accuracy of your device
- Urban areas typically have better GPS precision
- The tool finds the nearest location in our database, which may not be your exact address
- If no nearby location is found, consider [contributing](contribute.md) your location to the database

## Technical Details

This tool demonstrates practical usage of the LocationDB API for proximity-based location lookup, a common use case for location-based applications.
