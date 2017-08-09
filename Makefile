#########
#  API  #
#########

API_IMAGE_NAME=restful-coffee-api
DEV_PORT=8080

build:
	docker build -t $(API_IMAGE_NAME):latest .

run: build
	docker run --rm -v $(PWD):/usr/src/app -p 8080:8080 $(API_IMAGE_NAME)

dev: build
	docker run -it -v $(PWD):/usr/src/app -p 8080:8080 $(API_IMAGE_NAME) bash


################
#  OPERATIONS  #
################

migrate:
	./manage.py makemigrations
	./manage.py migrate


##################
#   DEVELOPMENT  #
##################

# Commands to be run inside the Docker container during development.

dev-server:
	pip install -r requirements/local.txt
	DJANGO_DEBUG=True ./manage.py runserver_plus 0.0.0.0:$(DEV_PORT)
