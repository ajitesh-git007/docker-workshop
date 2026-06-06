# building the base image
FROM python:3.13.11-slim 

# importing the pre-requisites 
RUN pip install pandas pyarrow 

# set-up the working directory 
WORKDIR /app 

# copy the code file into the docker environment 
COPY pipeline.py pipeline.py 

# setting up the entrypoint 
# ENTRYPOINT ["python", "pipeline.py"] 

# to execute the above docker file - 
# step - 1 -> build docker image => doucker build -t {nameofimage}:{tag} .
# step -2 -> run docker container