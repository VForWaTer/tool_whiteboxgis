# WhiteboxGIS Tool

[![Docker Image CI](https://github.com/VForWaTer/tool_whiteboxgis/actions/workflows/docker-image.yml/badge.svg)](https://github.com/VForWaTer/tool_whiteboxgis/actions/workflows/docker-image.yml)
[![DOI](https://zenodo.org/badge/610682357.svg)](https://zenodo.org/badge/latestdoi/610682357)

This is a containerized version of WhiteboxGIS tools that implements workflows for a number of analyses. It follows the Tool Specification for reusable research software using Docker.

## Tools

### WhiteboxGIS Version Info
**Description:** Returns the output of WhiteboxGIS version information.

**Parameters:**
- `toFile` (bool): If `True`, an `INFO.txt` file will be written (default: `true`).

---

### CATFLOW Hillslope Generator
**Description:** Produces the required raster (.TIFF) files for running the CATFLOW Hillslope Wizard Tool using [Whitebox GIS](https://www.whiteboxgeo.com/).

**Parameters:**
- `stream_threshold` (float): Threshold in flow accumulation values for channelization (extracting streams).

**Data:**
- `dem` (file): The input DEM file to be used for running the tool (.TIFF/.TIF format).
  - Example: `/in/dem.tif`.

---

### Merge TIFF Files
**Description:** Merges multiple TIFF files into a single raster file using [Whitebox GIS](https://www.whiteboxgeo.com/).

**Parameters:**
- `method` (string): Resampling method to use for merging. Options are:
  - `nn`: Nearest Neighbor.
  - `bilinear`: Bilinear Interpolation.
  - `cc`: Cubic Convolution.

**Data:**
- `in_file` (directory): Input directory containing TIFF files to merge (.TIFF/.TIF format).
  - Example: `/in/tiff_files/`.

**Output:**
- Merged raster file saved to `/out/dem.tif`.


