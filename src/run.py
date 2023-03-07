import os
from datetime import datetime as dt
from pprint import pprint

from json2args import get_parameter

# parse parameters
kwargs = get_parameter()

# check if a toolname was set in env
toolname = os.environ.get('TOOL_RUN', 'foobar').lower()

# switch the tool
if toolname == 'foobar':
    # RUN the tool here and create the output in /out
    print('This toolbox does not include any tool. Did you run the template?\n')
    
    # write parameters to STDOUT.log
    pprint(kwargs)

# In any other case, it was not clear which tool to run
else:
    raise AttributeError(f"[{dt.now().isocalendar()}] Either no TOOL_RUN environment variable available, or '{toolname}' is not valid.\n")
