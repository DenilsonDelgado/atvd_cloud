import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import global_settings
from router import api_router


app = FastAPI(title='Atividade de Cloud API',
              version='0.0.1',
              description="API desenvolvida para fins da atividade de Cloud")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
)

app.include_router(api_router,
                   prefix=global_settings.API_V_STR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app",
                log_level='info', reload=True)