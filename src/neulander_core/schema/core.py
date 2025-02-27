from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field, HttpUrl


##############################################################################
# Generic Schema for API request payload
##############################################################################
class DocIn(BaseModel):
    """
    DocIn is a Pydantic model representing a document input with the following attributes:
    Attributes:
        docid (str): Unique document identifier. This should resolve to a blobname if src is a SAS URL to a container.
        src (Any): Source of the document.
        dest (Any): Destination of the document.
        docmeta (Optional[str | dict]): Metadata associated with the document.
    """

    docid: str = Field(description="Unique document or blob name.")
    docpath: str = Field(
        description="Path to document from root (/). Will be used for src and ignored for dest."
    )
    src: Any
    dest: Any
    docmeta: Optional[str | dict] = Field(
        description="Metadata associated with the document"
    )


class AzureBlobDocIn(DocIn):
    """
    AzureBlobDocIn is a data model for handling Azure Blob Storage document input.
    Inherits from DocIn with the following attributes:
    Attributes:
        docid (str): Unique document identifier. This should resolve to a blobname if src is a SAS URL to a container.
        src (HttpUrl): SAS URL for the Azure blob container that contains the raw documents to be parsed.
        dest (HttpUrl): SAS URL for the Azure blob container where the parsed documents will be stored.
        docmeta (Optional[str | dict]): Metadata associated with the document.
    """

    src: HttpUrl = Field(
        description="SAS url for Azure blob container that has the raw documents to be parsed."
    )
    dest: HttpUrl = Field(
        description="SAS url for Azure blob container where the parsed documents will be stored."
    )


##############################################################################
# Generic Schema for all worker outputs
##############################################################################


class DocOut(BaseModel):
    docid: str = Field(
        description="Unique document identifier. This will be used to construct the output file name."
    )
    response: dict = Field(description="The response returned by the worker.")


##############################################################################
# API Responses
##############################################################################
class PublishResponse(BaseModel):
    """
    PublishResponse is a model representing the response of a publish operation.
    Attributes:
        docid (str): Unique document identifier. This should resolve to a blobname if src is a SAS URL to a container.
        response (Any): The response content of the publish operation.
        worker_name (str): The name of the worker that processed the publish operation.
        submission_ts (datetime): The timestamp when the submission was made.
    """

    docid: str = Field(
        description="Unique document identifier. This should resolve to a blobname if src is a SAS url to a container."
    )
    response: Any
    queue_name: str
    submission_ts: datetime
