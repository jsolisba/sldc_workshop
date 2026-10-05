from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return {
        "application": "DevOps SDLC Demo",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)