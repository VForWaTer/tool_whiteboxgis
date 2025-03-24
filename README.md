# WhiteboxGIS tool

[![Docker Image CI](https://github.com/VForWaTer/tool_whiteboxgis/actions/workflows/docker-image.yml/badge.svg)](https://github.com/VForWaTer/tool_whiteboxgis/actions/workflows/docker-image.yml)
[![DOI](https://zenodo.org/badge/610682357.svg)](https://zenodo.org/badge/latestdoi/610682357)

This is a containerized version of Whiteboxgis tools, that implements workflows for a number of analyses. It follows the Tool Specification for reusable research software using Docker.

## Tools

### WhiteboxGIS version info
**Description:** Return the output of WhiteboxGIS version information

**Parameters:**
- `toFile` (bool): If True, an INFO.txt will be written (default: true)

### CATFLOW Hillslope Generator
**Description:** Produces the required Raster (.TIFF) files for running the CATFLOW Hillslope Wizard Tool using [Whitebox GIS](https://www.whiteboxgeo.com/)

**Parameters:**
- `stream_threshold` (float): Threshold in flow accumulation values for channelization (extracting streams)

**Data:**
- `dem` (file): The Input DEM file to be used for running the tool (.TIFF/.TIF format)
  - Example: `/in/dem.tif`
  

