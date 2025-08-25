# WhiteboxGIS Workflows

This repository provides a containerized suite of [WhiteboxGIS](https://www.whiteboxgeo.com/) tools for geospatial raster analysis, including:

- **CATFLOW Hillslope Generator:** Generate raster files for CATFLOW hydrological modeling.
- **Merge TIFF Files:** Merge multiple raster files into a single output.
- **Reproject to Metric CRS:** Reproject rasters to a metric coordinate system (e.g., EPSG:25832).

It follows the [Tool Specification](https://vforwater.github.io/tool-specs) for reusable research software using Docker.

## Accessing the Container

You can use the pre-built container image directly from the GitHub Container Registry without building or installing Docker locally.

To pull the latest release, use:

```sh
docker pull ghcr.io/vforwater/tbr_whitebox:latest
```

You can then run the tools as described in the main [README.md](./README.md).