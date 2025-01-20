from typing import Dict, List

from pydantic import BaseModel

##############################################################################
# MedCAT Document Input
##############################################################################


class DocIn(BaseModel):
    id: int | str
    src: str
    dest: str


##############################################################################
# MedCAT Output Pydantic Models
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


class MetaAnnotations(BaseModel):
    Presence: PresenceMetaAnnotation
    Subject: SubjectMetaAnnotation
    Time: TimeMetaAnnotation


class MedcatOutput(BaseModel):
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
    meta_anns: MetaAnnotations


class DocOut(BaseModel):
    id: str | int
    text: str
    entities: Dict[int, MedcatOutput]
    doc_meta: dict
    model_meta: dict
