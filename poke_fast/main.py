from typing import Dict, List, Optional, Any
from fastapi import FastAPI, status, Depends
from time import sleep
from fastapi.responses import JSONResponse
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from fastapi import HTTPException
from models import pokemons, Pokemon

app = FastAPI(
    title='API de Pokemons',
    version='0.0.1',
    description='Uma API Fast'
)

def fake_db():
    try:
        print('Abrindo conexão com banco de dados...')
        sleep(1)
    finally:
        print('Fechando conexão com banco de dados...')
        sleep(1)

@app.get('/', response_model=str)
async def rota_raiz():
    return "Bem-vindo à API de Pokemons!"

@app.get('/pokemons',
         description='Retorna todos os pokemons ou uma lista vazia.',
         summary='Retorna todos os pokemons',
         response_model=List[Pokemon],
         response_description='Pokemons encontrados com sucesso.')
async def get_pokemons(db: Any = Depends(fake_db)):
    return pokemons

@app.post('/pokemons', status_code=status.HTTP_201_CREATED, response_model=Pokemon)
async def post_pokemons(pokemon: Pokemon):
    next_id: int = len(pokemons) + 1
    pokemon.id = next_id
    pokemons.append(pokemon)
    return pokemon

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=5001, reload=True)
