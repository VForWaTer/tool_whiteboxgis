from wbt import wbt

def print_info(to_file: bool):
    info = wbt.version()

    # write to file if needed
    if to_file:
        with open('/out/INFO.txt', 'w') as f:
            f.write(info)

    # output 
    print(info)

def fill(inp,out,flats):

    wbt.fill_depressions(
    inp, 
    out, 
    flats
    )

