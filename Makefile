# Variables
IMAGE_NAME := my_model
CONTAINER_NAME := my_model_container

# Build Docker image
build:
    docker build -t $(IMAGE_NAME) .

# Run Docker container
run:
    docker run -d -p 5000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Stop Docker container
stop:
    docker stop $(CONTAINER_NAME)

# Remove Docker container
remove:
    docker rm $(CONTAINER_NAME)

# Remove Docker image
clean:
    docker rmi $(IMAGE_NAME)

# Rebuild Docker image and run container
rebuild: clean build run

# Show Docker container logs
logs:
    docker logs $(CONTAINER_NAME)
