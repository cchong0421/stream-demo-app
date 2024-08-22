# Streamlit Demo

## Docker build image

```bash
# Build a docker image 
docker build -t <image_name> .

# Run container
docker run -p 8080:8080 <image_name>
```

## Installation

```bash
git clone 
cd stream-demo-app

docker-compose up -d --build

or

docker build -t streamlit-demo-app.1.0.0 .
```

The container will start in detached mode and can now be accessed via [localhost:8080](http://localhost:8080). Whenever you change the app/main.py the steamlit application will update too. If you want to build upon that example, just add your dependencies to the Dockerfile and rebuild the image using docker-compose.

After you are done, and you want to tear down the application, either

```bash
docker-compose stop
```

to stop the application, or use

```bash
docker-compose down --rmi all
```

to stop the application, remove the stopped containers and optionally `--rmi all` / remove all images associated in the docker-compose.yml file.
