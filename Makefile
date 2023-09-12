# Makefile for Flask App

# Define the default target
.DEFAULT_GOAL := help

# Variables
APP_NAME := lnkedin_video_downloader
DOCKER_IMAGE_NAME := $(APP_NAME)
DOCKER_CONTAINER_NAME := $(APP_NAME)-container
FLASK_ENV ?= production

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE_NAME) .

# Run the Docker container for development
run-dev:
	docker run -e FLASK_ENV=development -p 5000:5000 --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

# Run the Docker container for production
run-prod:
	docker run -e FLASK_ENV=production -p 5000:5000 --name $(DOCKER_CONTAINER_NAME) $(DOCKER_IMAGE_NAME)

# Stop and remove the Docker container
stop:
	docker stop $(DOCKER_CONTAINER_NAME) && docker rm $(DOCKER_CONTAINER_NAME)

# Clean up the Docker image
clean:
	docker rmi $(DOCKER_IMAGE_NAME)

# Show help message
help:
	@echo "Available targets:"
	@echo "  docker-build       Build the Docker image"
	@echo "  docker-run-dev     Run the Docker container for development"
	@echo "  docker-run-prod    Run the Docker container for production"
	@echo "  docker-stop        Stop and remove the Docker container"
	@echo "  docker-clean       Clean up the Docker image"
	@echo "  help               Show this help message"
