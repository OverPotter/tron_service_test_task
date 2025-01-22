from fastapi import FastAPI

from src.api.endpoints import router

app = FastAPI(
    title="TronService",
    version="0.0.1",
    docs_url="/api/v1/tron-service/docs",
    redoc_url="/api/v1/tron-service/redoc",
    openapi_url="/api/v1/tron-service/openapi.json",
)

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.rest_main:app", host="0.0.0.0", port=8000, reload=True)
