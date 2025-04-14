# Docker Fundamentals For Beginners and Project Ideas

## Need for Docker
1. Problem of environment separation for applications.
2. Problem of resource sharing.
3. Problem of portability.
4. Problem of easy scalability.
5. Problem of doing all this in a secured manner.

## Evolution of solutions
1. Virtual Machines or VM
2. Docker
   ![Docker vs VMs](https://miro.medium.com/max/1024/1*66cp6uoqv-q2clolRgSRJg.png)
3. Advantages of Docker
   1. All container share same kernel - thus storages is saved.
   2. Container boot time is less.
   3. Support for version control.
   4. Multiple container can start from single docker image and communicate.
   5. Images can be built on top of another.
   
## Installing docker to yours system.
1. [Install docker](https://docs.docker.com/get-docker/).
2. Initiate docker.
3. Check if it's working by ```docker version``` or ```docker-compose version```.

## Docker Image vs Container
1. Images are blueprint and container their instance.
3. To create image, we need to write instruction in ```Dockerfile``` and to create the container run the image.

## Docker Compose vs Dockerfile
1. Dockerfile describes how to build the image, ```docker-compose``` is used to run containers from ```docker-compose.yaml```.
2. ```docker-compose.yaml``` can have reference to Dockerfile but not the other way around.
3. Sample ```Dockerfile```
   ```
   FROM alpine:latest

   RUN apk update && \
       apk add curl && \
       apk add git && \
       apk add vim
   ```
   
   Sample ```docker-compose.yaml```
   ```
   version: "3.9"
   services:
     web:
       build: .
       ports:
         - "8000:5000"
     redis:
       image: "redis:alpine"

   ```

## Beginner Project Ideas Using Docker
1. [Learn common commands for docker](https://docs.docker.com/engine/reference/commandline/docker/).
2. [Learn common docker-compose commands](https://docs.docker.com/engine/reference/commandline/compose/).
3. [Create account in Docker Hub and play around](https://hub.docker.com/).
4. [Create RestAPIs and host them in Heroku using Docker](https://devcenter.heroku.com/categories/deploying-with-docker).
5. [Work with common tools like Airflow where multiple containers interact](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
6. Build your microservices with Docker.

## Walkthrough
[![Top Docker project ideas for beginners | Installing Docker | Docker tutorial | Naukri Learning](https://yt-embed.herokuapp.com/embed?v=-Hnpt0QyejU)](https://youtu.be/-Hnpt0QyejU "Top Docker project ideas for beginners | Installing Docker | Docker tutorial | Naukri Learning ")
