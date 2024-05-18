from pydantic import BaseModel, ConfigDict

class BaseSchema(BaseModel):
    pass

class IDSchemaMixin(BaseModel):
    model_config = ConfigDict(extra='allow')

    id: int
