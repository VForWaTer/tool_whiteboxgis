import os
import sys
from datetime import datetime as dt
from pprint import pprint

from json2args import get_parameter
import lib as wblib

# parse parameters
kwargs = get_parameter()

# check if a toolname was set in env
toolname = os.environ.get('TOOL_RUN', 'whitebox_info').lower()

# switch the tool
if toolname == 'whitebox_info':
    wblib.print_info(to_file=kwargs.get('toFile', True))

 # Tool for generating required Raster files for CATFLOW Hillslope Wizard
elif toolname == 'hillslope_generator':
    # get the parameters
    try:
        inp = kwargs['dem']
        clip = kwargs.get('clip_extent', False)
        shp = kwargs.get('basins', '/in/basin.shp')
        thres = kwargs.get('stream_threshold', 100.0)
    except Exception as e:
        print(str(e))
        sys.exit(1)
        
    if(clip):
        wblib.clip(inp,inp,shp)   
    
    # Define the output file locations
    filled = '/out/fill_DEM.tif'
    aspect = '/out/aspect.tif'
    accu = '/out/flow_accumulation.tif'
    flowdir = '/out/flow_direction.tif'
    streams = '/out/streams.tif'
    hillslope = '/out/hillslopes.tif'
    elevation = '/out/elevation.tif'
    distance = '/out/distance.tif'

    # run the whitebox fill_depression algorithm
    print(f"Filling depressions in DEM '{inp}'...",end='',flush=True)
    wblib.fill(inp,filled)
    print('done.')

    #Aspect algorithm
    print(f"Calculating Slope Aspect in DEM '{filled}'...",end='',flush=True)
    wblib.aspect(filled,aspect)
    print('done.')    

    #Flow Accumulation Algorithm
    print(f"Calculating Flow Accumulation  DEM '{filled}'...",end='',flush=True)
    wblib.accu_d8(filled,accu)
    print('done.')       
    
   #Flow Direction Algorithm
    print(f"Calculating Flow Direction '{filled}'...",end='',flush=True)
    wblib.dir_d8(filled,flowdir)
    print('done.')  

   #Stream Extraction tool
    print(f"Stream Extraction from '{accu}'...",end='',flush=True)
    wblib.stream(accu,streams,thres)
    print('done.')     

   #Hillslope Extraction tool
    print(f"Hillslope Extraction from  '{flowdir}'...",end='',flush=True)
    wblib.hillslope(flowdir,hillslope,streams)
    print('done.')    

  #Elevation to River tool
    print(f" Distance and Elevation from River '{streams}'...", end='', flush=True)
    wblib.distance(filled, elevation, streams)
    wblib.elevation(filled, distance, streams)
    print('done.')   

# In any other case, it was not clear which tool to run
else:
    raise AttributeError(f"[{dt.now().isocalendar()}] Either no TOOL_RUN environment variable available, or '{toolname}' is not valid.\n")
