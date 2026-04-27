from pydantic import BaseModel

class SpellRequest(BaseModel):
    description: str