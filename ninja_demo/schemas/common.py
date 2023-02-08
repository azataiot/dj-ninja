# ninja_demo/schemas / one.py
# Created by azat at 8.02.2023
import uuid
from datetime import datetime

from ninja import Schema
from ninja.orm import create_schema
from ninja_demo.models import One, Two

OneSchema = create_schema(One, depth=0)
TwoSchema = create_schema(Two, depth=0)

OneSchemaDeep = create_schema(One, depth=1)
TwoSchemaDeep = create_schema(Two, depth=1)


class OneSchemaFullManually(Schema):
    uid: uuid.UUID
    slug: str
    created: datetime
    last_updated: datetime
