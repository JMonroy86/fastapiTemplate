import uvicorn
from fastapi import FastAPI
from core.config import Settings
from db.db_config import engine, database, metadata
from apis.base import api_router


from utils import get_logger

logger = get_logger(__name__)


app = FastAPI(title=Settings.PROJECT_NAME, version=Settings.PROJECT_VERSION)


def include_router():
    app.include_router(api_router)


async def start_db():
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)
        logger.info("Database connected successfully")

    # for AsyncEngine created in function scope, close and
    # clean-up pooled connections
    await engine.dispose()


@app.on_event("startup")
async def startup_event():
    logger.info("Starting up...")
    await start_db()
    include_router()
    logger.info("Routes loaded successfully")


@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down...")
    await database.disconnect()
    logger.info("Database disconnected successfully")


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
