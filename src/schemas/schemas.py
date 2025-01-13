from pydantic import BaseModel, Field, model_validator
from typing import Optional


class StarshipParams(BaseModel):
    starship_id: int = Field(..., ge=2, le=75,
                             description="IDs permitidos estão entre 2 e 75.")
    page: int = Field(..., ge=1, le=35,
                      description="Número da página deve estar entre 1 e 35.")
    limit: int = Field(..., ge=1, le=10,
                       description="Limite máximo é 10 itens por página.")


class StarshipListParams(BaseModel):

    page: int = Field(..., ge=1, le=35,
                      description="Número da página deve estar entre 1 e 35.")
    limit: int = Field(..., ge=1, le=10,
                       description="Limite máximo é 10 itens por página.")
