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

 # Fill Depression tool
elif toolname == 'fill_depressions':
    # get the parameters
    try:
        inp = kwargs['inputDEM']
        out = '/out/filled_DEM.tif'
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
        inp = kwargs['filled_DEM']
        out = '/out/aspect_DEM.tif'
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
        inp = kwargs['filled_DEM']
        out = '/out/flow_accu_DEM.tif'
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
        inp = kwargs['filled_DEM']
        out = '/out/flow_dir_DEM.tif'
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the whitebox algorithm
    print(f"Calculating Flow Direction DEM '{inp}'...",end='',flush=True)
    wblib.dir_d8(inp,out)
    print('done.')  

 # Stream Extraction tool
elif toolname == 'stream_extraction':
    # get the parameters
    try:
        inp = kwargs['flow_accu_DEM']
        out = '/out/stream_DEM.tif'
        thres = kwargs['threshold']
    except Exception as e:
        print(str(e))
        sys.exit(1)

    # run the whitebox algorithm
    print(f"Stream Extraction from DEM '{inp}'...",end='',flush=True)
    wblib.stream(inp,out,thres)
    print('done.')      

# In any other case, it was not clear which tool to run
else:
    raise AttributeError(f"[{dt.now().isocalendar()}] Either no TOOL_RUN environment variable available, or '{toolname}' is not valid.\n")
