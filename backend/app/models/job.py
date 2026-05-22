from pydantic import BaseModel


class JobInput(BaseModel):
    title: str
    company: str
    description: str
    salary: str | None = None
    location: str | None = None