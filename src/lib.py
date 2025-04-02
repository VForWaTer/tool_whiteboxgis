from wbt import wbt
from json2args.logger import logger
import os
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

def mosaic_tool(input_dir, output_file, method):
    # Ensure the input directory exists
    if not os.path.exists(input_dir):
        logger.error(f"Input directory '{input_dir}' does not exist.")
        return

    # Gather all TIFF files in the input directory
    input_files = list(Path(input_dir).glob("*.tif"))
    if not input_files:
        logger.error(f"No TIFF files found in '{input_dir}'.")
        return

    # Convert input files to a comma-separated string
    input_files_str = ",".join(str(file) for file in input_files)

    # Log the input files being processed
    logger.info(f"Mosaicking the following files: {input_files_str}")

    # Execute the mosaic function
    try:
        wbt.mosaic(inputs=input_files_str, output=output_file, method=method)
        logger.info(f"Mosaic created successfully and saved to '{output_file}'.")
    except Exception as e:
        logger.error(f"An error occurred while creating the mosaic: {e}")
