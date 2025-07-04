# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a location database project that provides geolocation data in multiple formats. The project consists of:
- A hierarchical YAML-based database of global locations with coordinates
- Python tools for data processing and API generation
- MkDocs-based documentation site
- API endpoints serving location data in JSON format

## Development Commands

### Documentation Site
```bash
# Build and serve documentation locally
mkdocs serve

# Build documentation for production
mkdocs build
```

### Data Processing
```bash
# Generate data files from YAML database
cd tools
python from_database.py

# Import data from Google Sheets (requires GOOGLE_SHEET env var)
python to_database.py

# Test data processing
python merge.py
```

### Python Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

## Architecture

### Database Structure
- **Location**: `database/` - Hierarchical YAML files organized by continent/region/country/admin1/admin2/city/suburb
- **Schema**: Each YAML file contains: `id` (UUID), `latitude`, `longitude`, `postcode`
- **Hierarchy**: Geographic hierarchy is inferred from file path structure

### Data Processing Pipeline
1. **Source**: YAML files in `database/` directory
2. **Processing**: `tools/from_database.py` reads all YAML files and validates unique IDs
3. **Output**: Generates paginated JSON files (`docs/data.json`, `docs/data1.json`, etc.) with 100 records per page
4. **Documentation**: Updates `docs/index.md` with current record count and pagination info

### Key Components

#### tools/from_database.py
Main data processing script that:
- Traverses database directory recursively
- Validates unique IDs across all location records
- Extracts geographic hierarchy from file paths
- Generates paginated JSON files (100 records per page)
- Updates documentation with current statistics and pagination info

#### tools/location.py
Client library for accessing the location API:
- Provides `locationdb` class for downloading location data
- Supports pagination with options to download all pages or single page
- Includes `get_page_info()` method for pagination metadata
- Used for programmatic access to the dataset

#### tools/to_database.py
Data import utility:
- Imports location data from Google Sheets
- Creates new YAML files in proper hierarchy
- Generates unique UUIDs for new locations
- Integrates with git for version control

### Data Validation
- All location records must have unique UUIDs
- Missing IDs cause validation failures
- Duplicate IDs are detected and reported
- Build process exits with error if validation fails

## File Organization

```
database/           # YAML location database (hierarchical)
docs/              # MkDocs documentation and generated data files
tools/             # Python processing and utility scripts
requirements.txt   # Python dependencies
mkdocs.yml        # Documentation configuration
```

## Important Notes

- The database uses geographic file paths to infer location hierarchy
- ID validation is strict - all records must have unique UUIDs
- Documentation is auto-generated from the database content
- The API uses pagination with 100 records per page (data.json, data1.json, data2.json, etc.)
- All data processing should be done through the tools/ scripts

## Pagination Details

- **Page Size**: 100 records per page
- **File Naming**: `data.json` (page 0), `data1.json` (page 1), `data2.json` (page 2), etc.
- **Metadata**: Each page includes `total`, `total_pages`, `page`, `records`, and `next_page` fields
- **Navigation**: Use `next_page` URL to traverse pages, or access pages directly by filename