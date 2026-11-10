# Streamlit Demo

## 開發環境設定

### 方法一：使用 uv（推薦）

1. 安裝 [uv](https://docs.astral.sh/uv/)（若尚未安裝）：
    ```bash
    # macOS / Linux
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. 同步依賴與虛擬環境：
    ```bash
    uv sync
    ```

3. 啟動 Streamlit 應用程式：
    ```bash
    uv run streamlit run app/main.py
    ```

> **提示**：請使用 `uv run streamlit run app/main.py` 啟動。若直接執行 `uv run app/main.py` 會以純 Python 腳本模式運行，缺少 Streamlit runtime context 而無法開啟 Web 服務。

---

### 方法二：傳統 Python venv + pip

1. 安裝 Python 3.11.3 或更高版本
2. 建立並啟用虛擬環境：
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # macOS / Linux
    # Windows 請執行: .venv\Scripts\activate
    ```
3. 安裝套件：
    ```bash
    pip install -r requirements.txt
    ```
4. 啟動範例程式：
    ```bash
    streamlit run app/main.py
    ```

---

## Docker build image

```bash
# Build a docker image 
docker build -t <image_name> .

# Run container
docker run -p 8080:8080 <image_name>
```

## Installation

```bash
git clone <repository_url>
cd stream-demo-app

docker-compose up -d --build

# or

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
