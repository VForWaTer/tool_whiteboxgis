# WhiteboxGIS Tool

[![Docker Image CI](https://github.com/VForWaTer/tool_whiteboxgis/actions/workflows/docker-image.yml/badge.svg)](https://github.com/VForWaTer/tool_whiteboxgis/actions/workflows/docker-image.yml)
[![DOI](https://zenodo.org/badge/610682357.svg)](https://zenodo.org/badge/latestdoi/610682357)

**About Whitebox:**  
[Whitebox](https://www.whiteboxgeo.com/) is an advanced open-source geospatial analysis platform. It provides a wide range of tools for processing raster and vector geospatial data, with a focus on terrain analysis, hydrology, and environmental modeling. Whitebox is designed for both researchers and professionals, offering a user-friendly interface and powerful scripting capabilities.

This is a containerized version of WhiteboxGIS tools that implements workflows for a number of analyses. It follows the [Tool Specification](https://vforwater.github.io/tool-specs/) for reusable research software using Docker.

**Docker Image Updates:**  
You can always pull the latest released version of this tool from the GitHub Container Registry using:
```sh
docker pull ghcr.io/vforwater/tbr_whitebox:latest
```
or rebuild locally to get the newest features and fixes.

---

## Table of Contents

- [Tools](#tools)
- [Usage](#usage)
- [Input and Output](#input-and-output)
- [Running with Docker](#running-with-docker)
- [Development](#development)
- [License](#license)
- [References](#references)

---

## Tools

### CATFLOW Hillslope Generator
**Description:** Produces the required raster (.TIFF) files for running the CATFLOW Hillslope Wizard Tool using [Whitebox GIS](https://www.whiteboxgeo.com/).

**Parameters:**
- `stream_threshold` (float): Threshold in flow accumulation values for channelization (extracting streams).

**Data:**
- `dem` (file): The input DEM file to be used for running the tool (.TIFF/.TIF format).
  - Example: `/in/dem.tif`.

**Output:**
- Multiple raster files including filled DEM, aspect, flow accumulation, flow direction, streams, hillslopes, elevation above stream, and downslope distance to stream, saved to `/out/`.

---

### Merge TIFF Files
**Description:** Merges multiple TIFF files into a single raster file using [Whitebox GIS](https://www.whiteboxgeo.com/).

**Parameters:**
- `method` (string): Resampling method to use for merging. Options are:
  - `nn`: Nearest Neighbor.
  - `bilinear`: Bilinear Interpolation.
  - `cc`: Cubic Convolution.

**Data:**
- `input_files` (list): List of input TIFF files to merge (.TIFF/.TIF format).
  - Example: `["/in/elevation_1100_part_1.tif", "/in/elevation_1100_part_2.tif"]` or `/in/*.tif`.

**Output:**
- Merged raster file saved to `/out/dem.tif`.

---

### Reproject to Metric CRS
**Description:** Reproject a raster into a metric CRS (defaults to EPSG:25832 for Karlsruhe/Baden‑Württemberg) with a specified cell size.

**Parameters:**
- `target_epsg` (integer, optional): Target EPSG code; if invalid or not provided, defaults to EPSG:25832.
- `cell_size` (number, optional, default: 30): Output pixel size in meters.
- `resampling` (string, optional, default: "bilinear"): Resampling method. Options: `"nearest"`, `"bilinear"`, `"cubic"`.

**Data:**
- `dem` (file): The input DEM file to be reprojected (.TIFF/.TIF format).
  - Example: `/in/dem.tif`.

**Output:**
- Reprojected raster file saved to `/out/reprojected.tif` (or specified output path).

---

## Usage

1. **Prepare Input Files:**  
   Place your input files (e.g., DEMs or TIFFs) in the `/in` directory.

2. **Configure Input JSON:**  
   Edit the `input.json` file to specify parameters and data for the desired tool.

   Example for merging TIFFs:
   ```json
   {
     "merge_tifs": {
       "parameters": {
         "method": "nn"
       },
       "data": {
         "input_files": [
           "/in/elevation_1100_part_1.tif",
           "/in/elevation_1100_part_2.tif"
         ]
       }
     }
   }
   ```

3. **Install Docker and Build the Container:**

   - **Install Docker:**  
     Download and install Docker Desktop from [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/) and follow the installation instructions for your operating system.

   - **Build the Docker image:**  
     Open a terminal or command prompt in the project directory and run:
     ```sh
     docker build -t whitebox .
     ```

4. **Run with Docker:**  
   Use the following command to run the tool (replace `whitebox` with your Docker image name):

   **Note:**  
   Make sure to mount your local input and output directories to the container's `/in` and `/out` directories using the `-v` option.  
   For example, if your local input files are in `local/in` and you want outputs in `local/out`, use:

   For **PowerShell**:
   ```powershell
   docker run --rm -it `
     -v "${PWD}/local/in:/in" `
     -v "${PWD}/local/out:/out" `
     -e TOOL_RUN=merge_tifs `
     whitebox
   ```

   For **Command Prompt**:
   ```cmd
   docker run --rm -it ^
     -v "%cd%/local/in:/in" ^
     -v "%cd%/local/out:/out" ^
     -e TOOL_RUN=merge_tifs ^
     whitebox
   ```

   *(Adjust the paths as needed for your environment.)*

---

## Input and Output

- **Input Directory (`/in`):**  
  Place all required input files here.  
  Example: `/in/dem.tif`, `/in/elevation_1100_part_1.tif`, etc.

- **Output Directory (`/out`):**  
  All generated files will be saved here.  
  Example: `/out/dem.tif`, `/out/fill_DEM.tif`, etc.

- **Input JSON Example (Merge TIFFs):**
  ```json
  {
    "merge_tifs": {
      "parameters": {
        "method": "nn"
      },
      "data": {
        "input_files": [
          "/in/elevation_1100_part_1.tif",
          "/in/elevation_1100_part_2.tif"
        ]
      }
    }
  }
  ```

- **Input JSON Example (CATFLOW Hillslope Generator):**
  ```json
  {
    "hillslope_generator": {
      "parameters": {
        "stream_threshold": 1000
      },
      "data": {
        "dem": "/in/dem.tif"
      }
    }
  }
  ```

- **Input JSON Example (Reproject to Metric CRS):**
  ```json
  {
    "reproject_to_metric": {
      "parameters": {
        "target_epsg": 25832,
        "cell_size": 30,
        "resampling": "bilinear",
        "source_epsg": 4326
      },
      "data": {
        "dem": "/in/dem.tif"
      }
    }
  }
  ```

---

## Running with Docker

- **Build the Docker image:**
  ```sh
  docker build -t whitebox .
  ```

- **Run the container:**
  (See [Usage](#usage) for platform-specific examples.)

---

## Development

- Source code is located in the `/src` directory.
- To add new tools or modify existing ones, edit the Python files in `/src` and update `tool.yml` as needed.
- Contributions are welcome! Please open issues or pull requests on GitHub.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## References

- [WhiteboxTools Documentation](https://www.whiteboxgeo.com/manual/wbt_book/available_tools/)
- [VForWaTer Tool Specification](https://github.com/VForWaTer/tool-specs)


