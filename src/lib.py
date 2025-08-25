from wbt import wbt
from json2args.logger import logger
import os
import rioxarray as rxr
from pyproj import CRS
from rasterio.enums import Resampling
from pathlib import Path

def print_info(to_file: bool):
    info = wbt.version()

    # write to file if needed
    if to_file:
        with open('/out/INFO.txt', 'w') as f:
            f.write(info)

    # output 
    print(info)

def clip(inp,out,shp):

    wbt.clip(
    i=inp, 
    clip=shp,
    output=out, 
    )

def fill(inp, out):
    wbt.fill_depressions(inp, out)


def aspect(inp,out):

    wbt.aspect(
    inp, 
    out, 
    )

def accu_d8(inp,out):

    wbt.d8_flow_accumulation(
    inp, 
    out, 
    out_type='cells', 
    )

def dir_d8(inp,out):

    wbt.d8_pointer(
    inp, 
    out, 
    )

def stream(inp,out,thres):

    wbt.extract_streams(
    inp, 
    out, 
    thres, 
    )   

def hillslope(inp,out,stream):

    wbt.hillslopes(
    d8_pntr = inp, 
    streams = stream, 
    output = out, 
    )  

def elevation(inp,out,stream):

    wbt.elevation_above_stream(
    dem = inp, 
    streams = stream, 
    output = out 
    )    

def distance(inp,out,stream):

    wbt.downslope_distance_to_stream(
    dem = inp, 
    streams = stream, 
    output = out 
    )   

def mosaic_tool(input_files, output_file, method):
    # Ensure the input files list is not empty
    if not input_files or not isinstance(input_files, list):
        logger.error("No input files provided for mosaicking.")
        return

    # Convert input files to a comma-separated string
    input_files_str = ",".join(input_files)

    # Log the input files being processed
    logger.info(f"Mosaicking the following files: {input_files_str}")

    # Execute the mosaic function
    try:
        wbt.mosaic(inputs=input_files_str, output=output_file, method=method)
        logger.info(f"Mosaic created successfully and saved to '{output_file}'.")
    except Exception as e:
        logger.error(f"An error occurred while creating the mosaic: {e}")


DEFAULT_EPSG = 25832  # ETRS89 / UTM 32N (Karlsruhe / Baden-Württemberg)

_RESAMPLE = {
    'nearest': Resampling.nearest,
    'bilinear': Resampling.bilinear,
    'cubic': Resampling.cubic,
}        

def _valid_epsg_or_default(epsg):
    """Return a valid EPSG integer or DEFAULT_EPSG if missing/invalid."""
    try:
        epsg_int = int(epsg)
        CRS.from_epsg(epsg_int)  # raises if invalid
        return epsg_int
    except Exception:
        return DEFAULT_EPSG

def _parse_resampling(name: str):
    return _RESAMPLE.get(str(name).lower(), Resampling.bilinear)


def reproject_to_metric(input_path: str,
                        output_path: str = "/out/reprojected.tif",
                        target_epsg=DEFAULT_EPSG,
                        cell_size=30,
                        resampling='bilinear'):
    """
    Reproject a raster to a metric projected CRS and save to file.
    Creates GeoTIFF in output_path. Does not return anything.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input raster not found: {input_path}")

    tgt_epsg = _valid_epsg_or_default(target_epsg)
    tgt_crs = CRS.from_epsg(tgt_epsg)
    resamp_enum = _parse_resampling(resampling)

    src = rxr.open_rasterio(input_path, masked=True)
    nodata = src.rio.nodata

    dst = src.rio.reproject(
        tgt_crs,
        resolution=float(cell_size),
        resampling=resamp_enum,
        nodata=nodata
    )

    dst.rio.to_raster(output_path, compress="DEFLATE")