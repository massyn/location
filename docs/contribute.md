# Contributing to LocationDB

LocationDB is a community-driven project that relies on contributions from users worldwide. Whether you're adding new locations, improving existing data, or enhancing the codebase, your contributions are valuable.

## Ways to Contribute

### 1. Add New Locations
Help expand our global coverage by adding missing locations to the database.

### 2. Improve Existing Data
Update coordinates, postal codes, or correct location information for better accuracy.

### 3. Code Contributions
Enhance the tools, API, or documentation to improve the project.

### 4. Report Issues
Found a problem? Report bugs or suggest improvements through GitHub issues.

## Adding New Locations

### Step 1: Understand the Structure

Each location is stored as a YAML file in a hierarchical directory structure representing the geographic hierarchy.

**Directory Structure:**
```
database/
├── continent/
│   ├── region/
│   │   ├── country/
│   │   │   ├── admin1/
│   │   │   │   ├── admin2/
│   │   │   │   │   ├── city/
│   │   │   │   │   │   ├── suburb/
│   │   │   │   │   │   │   └── location.yaml
```

### Step 2: Create the YAML File

Use this template for new locations:

```yaml
id: [unique-uuid]
latitude: [decimal-latitude]
longitude: [decimal-longitude]
postcode: "[postal-code]"
```

**Example:**
```yaml
id: 861af882-4a1e-4687-bae4-0ecb5caa9f55
latitude: -27.4698
longitude: 153.0251
postcode: "4000"
```

### Field Requirements

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | String (UUID) | ✅ | Unique identifier - generate at [uuidgenerator.net](https://www.uuidgenerator.net/) |
| `latitude` | Number | ✅ | Decimal latitude (-90 to 90) |
| `longitude` | Number | ✅ | Decimal longitude (-180 to 180) |
| `postcode` | String | ⚠️ | Postal/ZIP code (quote to preserve leading zeros) |

### Step 3: Understand the Geographic Hierarchy

The directory structure represents geographic hierarchy from broad to specific:

| Level | Description | Examples |
|-------|-------------|----------|
| **continent** | One of the seven continents | Africa, Asia, Europe, North America |
| **region** | Sub-continental grouping | Southeast Asia, Western Europe, Eastern Africa |
| **country** | ISO 3166 country name | Australia, United States, Germany |
| **admin1** | First administrative division | State, province, canton, region |
| **admin2** | Second administrative division | County, district, municipality |
| **city** | Named populated place | City, town, locality |
| **suburb** | Subdivision within a city | Suburb, village, neighborhood, district |

### Step 4: Place Your File

Create your YAML file in the appropriate directory path. The filename should match the location name.

**Example Path:**
```
database/Oceania/Australia and New Zealand/Australia/Queensland/South East Queensland/Brisbane/Brisbane.yaml
```

## Submission Process

### 1. Fork the Repository
Fork the [LocationDB repository](https://github.com/massyn/location) to your GitHub account.

### 2. Create a Branch
```bash
git checkout -b add-new-location
```

### 3. Add Your Location
Create the YAML file in the correct directory structure.

### 4. Test Your Changes
Run the validation script to ensure your data is correct:
```bash
cd tools
python from_database.py
```

### 5. Submit a Pull Request
Create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) with:
- Clear description of what you're adding
- Why the location is needed
- Source of coordinate data

## Data Quality Guidelines

### ✅ Do
- Use accurate coordinates from reliable sources
- Include postal codes when available
- Follow the established directory structure
- Generate a unique UUID for each location
- Test your changes before submitting

### ❌ Don't
- Duplicate existing locations
- Use approximate or guessed coordinates
- Change existing UUIDs
- Submit locations without proper hierarchy
- Include personal or sensitive information

## Important Rules

1. **UUID Permanence**: Once assigned, a UUID must never change. Applications depend on this stability.

2. **Coordinate Accuracy**: Use precise decimal coordinates from authoritative sources like:
   - OpenStreetMap
   - Google Maps
   - Government geographic databases
   - GPS devices

3. **Hierarchy Consistency**: Maintain consistent naming and structure within geographic regions.

4. **Data Validation**: All submissions are automatically validated for:
   - Unique UUIDs
   - Valid coordinate ranges
   - Required fields
   - Proper file structure

## Getting Help

- **Questions**: Open a [GitHub Discussion](https://github.com/massyn/location/discussions)
- **Issues**: Report problems via [GitHub Issues](https://github.com/massyn/location/issues)
- **Examples**: Browse existing locations for reference
- **Documentation**: Check the [API documentation](api.md) for technical details

Thank you for contributing to LocationDB and helping build a comprehensive global location database!