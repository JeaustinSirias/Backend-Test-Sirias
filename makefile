#############################################################
#							                                #
#                 Cornershop's Backend Test 		        #
#	   Jeaustin Sirias Chacón (jeaustin.sirias@gmail.com) 	#	    
#                     Copyright (C) 2020		            #
#							                                #
#############################################################

# VARIABLES 
TEST = ./test/
SOURCE = ./source/

# COMMANDS

docker:
	docker-compose build \
	&& docker-compose up

unittest:
	docker-compose build \
	&& docker-compose run --service-ports testing python3 manage.py test 

require: # Install requirements
	pip install -r requirements.txt

run: # Run project
	python3 manage.py runserver

