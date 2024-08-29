#!/bin/bash

# Update and install Docker
sudo apt-get update -y
sudo apt-get install docker.io -y

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Pull the Docker image for your application
docker pull your_docker_image_name

# Run the Docker container
docker run -d -p 80:80 your_docker_image_name

# Output the public IP address of the instance
curl http://169.254.169.254/latest/meta-data/public-ipv4