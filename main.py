import uvicorn
from fastapi import FastAPI
from core.config import Settings
from apis.base import api_router
from db.db_config import init_db


from utils import get_logger

logger = get_logger(__name__)


app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION)


async def start_db():
    app.state.pool = await init_db()
    logger.info("DB initialized successfully")


def include_router():
    app.include_router(api_router)


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    await start_db()
    include_router()
    logger.info("Routes loaded successfully")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")


def main():
    uvicorn.run(
        app="main:app",
        host='localhost',
        port=8000,
        reload=True,
        workers=1,
    )


if __name__ == '__main__':
    main()
