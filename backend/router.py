from fastapi import APIRouter
import httpx

api_router = APIRouter()

@api_router.get("/health_check")
async def get_health_check():
    return "Server is running"

@api_router.get("/joke")
async def get_joke():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get("https://v2.jokeapi.dev/joke/Any?lang=pt")
            joke_data = response.json()

            if joke_data.get("error", True):
                return {"error": "Não foi possível obter uma piada."}
            
            if joke_data["type"] == "single":
                return {
                    "category": joke_data["category"],
                    "joke": joke_data["joke"],
                    "safe": joke_data["safe"]
                }
            elif joke_data["type"] == "twopart":
                return {
                    "category": joke_data["category"],
                    "setup": joke_data["setup"],
                    "delivery": joke_data["delivery"],
                    "safe": joke_data["safe"]
                }
            else:
                return {"error": "Formato de piada desconhecido."}
        
        except httpx.RequestError:
            return {"error": "Falha ao conectar à API de piadas."}