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
    

# In any other case, it was not clear which tool to run
else:
    raise AttributeError(f"[{dt.now().isocalendar()}] Either no TOOL_RUN environment variable available, or '{toolname}' is not valid.\n")
