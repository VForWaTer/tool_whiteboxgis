from wbt import wbt


def print_info(to_file: bool):
    info = wbt.version()

    # write to file if needed
    if to_file:
        with open('/out/INFO.txt', 'w') as f:
            f.write(info)

    # output 
    print(info)

def clip(inp,out,shp):

    wbt.clip(
    i=inp, 
    clip=shp,
    output=out, 
    )

def fill(inp, out):
    wbt.fill_depressions(inp, out)


def aspect(inp,out):

    wbt.aspect(
    inp, 
    out, 
    )

def accu_d8(inp,out):

    wbt.d8_flow_accumulation(
    inp, 
    out, 
    out_type='cells', 
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