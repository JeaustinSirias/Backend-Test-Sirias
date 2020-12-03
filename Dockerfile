#############################################################
#							                                #
#             Cornershop's Backend Test solution	        #
#	                Jeaustin Sirias Chacón 		            #
#                    Copyright (C) 2020		                #
#							                                #
#############################################################
FROM python:3.8
ENV PYTHONUNBUFFERED=1

# The working directory in the container
WORKDIR /usr/src/app

# Get the project dependences
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Expose the 8000 default development port
EXPOSE 8000