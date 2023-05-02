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
        out = '/out/filled_dem.tif'
        flats = kwargs.get('fix_flats', True)
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the whitebox fill_depression algorithm
    print(f"Filling depressions in DEM '{inp}'...",end='',flush=True)
    wblib.fill(inp,out,flats)
    print('done.')

 # Aspect tool
elif toolname == 'aspect':
    # get the parameters
    try:
        inp = kwargs['dem']
        out = '/out/aspect.tif'
        zfactor = kwargs.get('z_factor', None)
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the whitebox fill_depression algorithm
    print(f"Calculating Slope Aspect in DEM '{inp}'...",end='',flush=True)
    wblib.aspect(inp,out,zfactor)
    print('done.')    

 # Flow Accumulation tool
elif toolname == 'flow_accumulation_d8':
    # get the parameters
    try:
        inp = kwargs['dem']
        out = '/out/flow_accumulation.tif'
        type = kwargs.get('out_type', 'cells')
        log = kwargs.get('log', False)
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the whitebox  algorithm
    print(f"Calculating Flow Accumulation  DEM '{inp}'...",end='',flush=True)
    wblib.accu_d8(inp,out,type,log)
    print('done.')       
    
 # Flow Direction tool
elif toolname == 'flow_direction_d8':
    # get the parameters
    try:
        inp = kwargs['dem']
        out = '/out/flow_direction.tif'
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the whitebox algorithm
    print(f"Calculating Flow Direction '{inp}'...",end='',flush=True)
    wblib.dir_d8(inp,out)
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
    wblib.stream(inp,out,thres)
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
