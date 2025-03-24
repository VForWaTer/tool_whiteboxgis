import os
import sys
from datetime import datetime as dt
from pathlib import Path

from json2args import get_parameter
from json2args.data import get_data_paths
from json2args.logger import logger
import lib as wblib

# parse parameters
kwargs = get_parameter(typed=True)
# check if a toolname was set in env
toolname = os.environ.get('TOOL_RUN', 'whitebox_info').lower()

# switch the tool
if toolname == 'whitebox_info':
    wblib.logger.info_info(to_file=kwargs.get('toFile', True))
    sys.exit(0)

# data is only needed for all but the info tool
data_paths = get_data_paths()
if 'dem' not in data_paths:
    logger.error("DEM not found in input data")
    sys.exit(1)

 # Tool for generating required Raster files for CATFLOW Hillslope Wizard
if toolname == 'hillslope_generator':
    # get the parameters
    #thres = kwargs.get('stream_threshold', 100.0)

    # Define the output file locations
    inp=data_paths['dem']
    filled = '/out/fill_DEM.tif'
    aspect = '/out/aspect.tif'
    accu = '/out/flow_accumulation.tif'
    flowdir = '/out/flow_direction.tif'
    streams = '/out/streams.tif'
    hillslope = '/out/hillslopes.tif'
    elevation = '/out/elevation.tif'
    distance = '/out/distance.tif'

    # run the whitebox fill_depression algorithm
    logger.info(f"Filling depressions in DEM '{inp}'...")
    wblib.fill(inp,filled)
    logger.info('done.')

    #Aspect algorithm
    logger.info(f"Calculating Slope Aspect in DEM '{filled}'...")
    wblib.aspect(filled,aspect)
    logger.info('done.')    

    #Flow Accumulation Algorithm
    logger.info(f"Calculating Flow Accumulation  DEM '{filled}'...")
    wblib.accu_d8(filled,accu)
    logger.info('done.')       
    
   #Flow Direction Algorithm
    logger.info(f"Calculating Flow Direction '{filled}'...")
    wblib.dir_d8(filled,flowdir)
    logger.info('done.')  

   #Stream Extraction tool
    logger.info(f"Stream Extraction from '{accu}'...")
    wblib.stream(accu,streams, kwargs.stream_threshold)
    logger.info('done.')     

   #Hillslope Extraction tool
    logger.info(f"Hillslope Extraction from  '{flowdir}'...")
    wblib.hillslope(flowdir,hillslope,streams)
    logger.info('done.')    

  #Elevation to River tool
    logger.info(f" Distance and Elevation from River '{streams}'...")
    wblib.distance(filled, elevation, streams)
    wblib.elevation(filled, distance, streams)
    logger.info('done.')   

# In any other case, it was not clear which tool to run
else:
    raise AttributeError(f"[{dt.now().isocalendar()}] Either no TOOL_RUN environment variable available, or '{toolname}' is not valid.\n")
