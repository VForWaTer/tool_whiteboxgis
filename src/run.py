import os
from datetime import datetime as dt
from pprint import pprint

from json2args import get_parameter
from wbt import wbt

# parse parameters
kwargs = get_parameter()

# check if a toolname was set in env
toolname = os.environ.get('TOOL_RUN', 'whitebox_info').lower()

# switch the tool
if toolname == 'whitebox_info':
    info = wbt.version()

    # write to file if needed
    if kwargs.get('toFile', True):
        with open('/out/INFO.txt', 'w') as f:
            f.write(info)

    # output 
    print(info)

# In any other case, it was not clear which tool to run
else:
    raise AttributeError(f"[{dt.now().isocalendar()}] Either no TOOL_RUN environment variable available, or '{toolname}' is not valid.\n")
