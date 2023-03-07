# Pull any base image that includes python3
FROM python:3.10

# install the toolbox runner tools
RUN pip install json2args


# create the tool input structure
RUN mkdir /in
COPY ./in /in
RUN mkdir /out
RUN mkdir /src
COPY ./src /src

# Install the Whiteboxgis toolbox here
RUN curl https://www.whiteboxgeo.com/WBT_Linux/WhiteboxTools_linux_amd64.zip -o /src/wbt.zip
WORKDIR /src
RUN unzip wbt.zip
RUN rm wbt.zip


CMD ["python", "run.py"]
