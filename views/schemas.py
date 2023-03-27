from datetime import datetime

from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int = Field(default=None, ge=1)
    title: str = Field(max_length=128)
    body: str
    slug: str = Field(default=None, max_length=128)
    author: str = Field(max_length=32)
    date_created: datetime = Field(default=datetime.now())

    @classmethod
    def from_sql(cls, data: list[tuple]):
        objs = []
        for obj in data:
            objs.append(
                cls(
                    id=obj[0],
                    title=obj[1],
                    body=obj[2],
                    slug=obj[3],
                    author=obj[4],
                    date_created=obj[5]
                )
            )
        return objs
