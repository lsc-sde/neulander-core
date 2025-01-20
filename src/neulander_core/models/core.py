from typing import Any

from pydantic import BaseModel


##############################################################################
# API Responses
##############################################################################
class PublishResponse(BaseModel):
    id: int | str
    response: Any
    queue: str
