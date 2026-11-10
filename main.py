from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from supabase import create_client, Client
import os

app = FastAPI()

# Permite que el frontend en Vercel se comunique con esta API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Las claves se leerán de forma segura desde Render
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

@app.get("/")
def read_root():
    return {"mensaje": "API de Crown Club funcionando 👑"}

@app.get("/products")
def get_productos():
    try:
        supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
        respuesta = supabase.table("products").select("*").execute()
        return respuesta.data
    except Exception as e:
        return {"error": str(e)}
