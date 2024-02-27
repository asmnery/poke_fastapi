from typing import Optional
from pydantic import BaseModel, validator

class Pokemon(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: str 
    habilidade: str 

    @validator('descricao')
    def validar_descricao(cls, value: str):
        # Validacao 1
        palavras = value.split(' ')
        if len(palavras) < 3:
            print("A descrição deve ter pelo menos 3 palavras.")
            #raise ValueError('A descrição deve ter pelo menos 3 palavras.')
        # Validacao 2
        if value.islower():
            print("A descrição deve ser capitalizada")
            #raise ValueError('A descrição deve ser capitalizada.')
        return value
pokemons = [
    Pokemon(id=1, nome='Pikachu', descricao='Pikachu é um tipo de Pokémon elétrico', habilidade ='Descarga Elétrica'),
    Pokemon(id=2, nome='Bulbasaur', descricao='Bulbasaur é um Pokémon bonito', habilidade ='Jato de Água'),
]
