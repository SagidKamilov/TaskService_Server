from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class UserSchemaAdd(BaseModel):
    id: int
    name: str


class UserSchemaDelete(BaseModel):
    id: int


class UserSchemaEdit(BaseModel):
    id: int
    name: str