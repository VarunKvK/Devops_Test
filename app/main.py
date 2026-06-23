from fastapi import FastAPI

app = FastAPI(
    title="DevOps Health Check API",
    version="1.0.0",
    description="A basic API project for learning CI/CD, Docker, and deployment.",
)

@app.get("/")
def root():
    return {
        "message": "DevOps Health Check API is running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "devops-health-api"
    }

@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }