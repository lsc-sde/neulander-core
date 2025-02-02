from typing import Dict, List, Optional

from pydantic import BaseModel, Field

##############################################################################
# MedCAT Output Schemas
##############################################################################


class BaseMetaAnnotation(BaseModel):
    name: str
    value: str
    confidence: float


class PresenceMetaAnnotation(BaseMetaAnnotation):
    pass


class SubjectMetaAnnotation(BaseMetaAnnotation):
    pass


class TimeMetaAnnotation(BaseMetaAnnotation):
    pass


class MetaAnnotation(BaseModel):
    Presence: PresenceMetaAnnotation
    Subject: SubjectMetaAnnotation
    Time: TimeMetaAnnotation


class MedcatEntity(BaseModel):
    pretty_name: str
    cui: str
    type_ids: List[str]
    types: List[str]
    source_value: str
    detected_name: str
    acc: float
    context_similarity: float
    start: int
    end: int
    icd10: List[str]
    ontologies: List[str]
    snomed: List[str]
    id: int
    meta_anns: MetaAnnotation


class MedcatOutput(BaseModel):
    docid: str = Field(description="Unique document identifier.")
    text: str = Field(description="Plain text of document that was parsed.")
    entities: Dict[int, MedcatEntity] = Field(
        description="Dictionary of entities detected in the document, keyed by entity ID."
    )
    docmeta: Optional[str | dict] = Field(
        description="Metadata associated with the document"
    )
    modelmeta: Optional[str | dict] = Field(
        description="Metadata associated with the MedCAT model used to annotate."
    )
