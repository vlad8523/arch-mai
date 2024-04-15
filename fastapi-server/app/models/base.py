from pydantic import BaseModel

class BaseSchema(BaseModel):
    pass

class IDSchemaMixin(BaseModel):
    id: int

    class Config(BaseModel.Config):
        orm_mode = True