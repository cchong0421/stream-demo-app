# Streamlit Demo

## 開發環境設定

- [] 安裝 Python 3.11.3 or higher
- [] 安裝 Visual studio code
- [] 安裝 Docker Desktop
- [] 安裝 python 套件(virtualenv)

    ```bash
    $ pip install virtualenv
    $ python -m venv .venv
    ```

- 啟動 Visual studio code 並從 Github clone .
- 按 <kbd>Ctrl</kbd> + <kbd>`</kbd> 啟動終端機視窗
- 然後執行下述指令

    ```bash
    # 啟動 python 虛擬環境
    $ pip install -r requirements.txt

    # 啟動範例程式
    $ streamlit run app/main.py
    ```

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
