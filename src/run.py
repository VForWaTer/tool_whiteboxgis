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
elif toolname == 'catflow_hillslope_generator':
    # get the parameters
    try:
        inp = kwargs['dem']
        clip = kwargs.get('clip_extent', False)
        shp = kwargs.get('shapefile', '/in/Shapefile.shp')
        thres = kwargs.get('stream_threshold', 100.0)
    except Exception as e:
        print(str(e))
        sys.exit(1)
    
    # Define the output file locations
    filled = '/out/fill_DEM.tif'
    aspect = '/out/aspect.tif'
    accu = '/out/flow_accumulation.tif'
    flowdir = '/out/flow_direction.tif'

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
    print(f"Calculating Flow Direction '{inp}'...",end='',flush=True)
    wblib.dir_d8(inp,flowdir)
    print('done.')  

 # Stream Extraction tool
elif toolname == 'stream_extraction':
    # get the parameters
    try:
        inp = kwargs['flow_accumulation']
        out = '/out/streams.tif'
        thres = kwargs['threshold']
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the whitebox algorithm
    print(f"Stream Extraction from '{inp}'...",end='',flush=True)
    wblib.stream(accu,out,thres)
    print('done.')     

 # Hillslope Extraction tool
elif toolname == 'hillslope_extraction':
    # get the parameters
    try:
        inp = kwargs['flow_direction']
        out = '/out/hillslopes.tif'
        stream = kwargs['stream']
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the whitebox algorithm
    print(f"Hillslope Extraction from  '{inp}'...",end='',flush=True)
    wblib.hillslope(inp,out,stream)
    print('done.')    

 # Elevation to River tool
elif toolname == 'stream_elev_dist':
    # get the parameters
    try:
        inp = kwargs['dem']
        out1 = '/out/elevation.tif'
        out2 = '/out/distance.tif'
        stream = kwargs['stream']
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the whitebox algorithm
    print(f" Distance and Elevation from River '{stream}'...", end='', flush=True)
    wblib.distance(inp, out2, stream)
    wblib.elevation(inp, out1, stream)
    print('done.')          
# In any other case, it was not clear which tool to run
else:
    raise AttributeError(f"[{dt.now().isocalendar()}] Either no TOOL_RUN environment variable available, or '{toolname}' is not valid.\n")
