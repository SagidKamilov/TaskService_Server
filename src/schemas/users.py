from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class UserSchemaGet(BaseModel):
    id: int
    name: str


class UserSchemaAdd(BaseModel):
    id: int
    name: str
