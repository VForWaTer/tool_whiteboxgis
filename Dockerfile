# Pull any base image that includes python3
# Lightweight base
FROM python:3.10-slim

# ---- System deps (minimal) ----
# curl + unzip to fetch WBT, and SSL certs for HTTPS
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    curl unzip ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# ---- Python deps ----
# json2args for your runner
# rioxarray + rasterio + pyproj for reprojection in Python
# xarray/numpy as rioxarray deps
# whitebox (Python wrapper) if you call WBT from Python anywhere
RUN pip install --no-cache-dir \
    json2args \
    numpy xarray \
    rasterio==1.3.10 \
    rioxarray \
    pyproj \
    whitebox

# (Optional) If you hit PROJ data lookup warnings, you can uncomment:
# ENV PROJ_NETWORK=ON

# ---- I/O + source layout ----
RUN mkdir -p /in /out /src
COPY ./in /in
COPY ./src /src

# ---- WhiteboxTools binary ----
# Download & unpack WBT into /src/WBT
RUN curl -fsSL https://www.whiteboxgeo.com/WBT_Linux/WhiteboxTools_linux_amd64.zip -o /src/wbt.zip && \
    cd /src && unzip -q wbt.zip && rm wbt.zip && \
    mv WhiteboxTools_linux_amd64/WBT /src/WBT && \
    rm -rf WhiteboxTools_linux_amd64

WORKDIR /src
CMD ["python", "run.py"]

