from wbt import wbt


def print_info(to_file: bool):
    info = wbt.version()

    # write to file if needed
    if to_file:
        with open('/out/INFO.txt', 'w') as f:
            f.write(info)

    # output 
    print(info)


def fill(inp, out, flats):
    wbt.fill_depressions(inp, out, flats)


def aspect(inp,out,zfactor):

    wbt.aspect(
    inp, 
    out, 
    zfactor
    )

def accu_d8(inp,out,type,log):

    wbt.d8_flow_accumulation(
    inp, 
    out, 
    out_type=type, 
    log=log, 
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