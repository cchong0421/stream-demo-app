# Streamlit Demo

## Installation

```bash
git clone 
cd streamlit-app-demo

docker-compose up -d --build
```

The container will start in detached mode and can now be accessed via [localhost:8000](http://localhost:8000). Whenever you change the app/main.py the steamlit application will update too. If you want to build upon that example, just add your dependencies to the Dockerfile and rebuild the image using docker-compose.

After you are done, and you want to tear down the application, either

```bash
docker-compose stop
```

to stop the application, or use

```bash
docker-compose down --rmi all
```

to stop the application, remove the stopped containers and optionally `--rmi all` / remove all images associated in the docker-compose.yml file.
