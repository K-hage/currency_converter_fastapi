from pydantic import BaseModel, validator


class Result(BaseModel):
    result: float

    @validator('result', pre=True)
    def set_result(cls, val):
        return round(val, 2)
