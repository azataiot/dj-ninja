# ninja_demo/schemas / user.py
# Created by azat at 8.02.2023
from datetime import datetime

from ninja import Schema
from ninja.orm import create_schema
from django.contrib.auth import get_user_model

from django.contrib.auth.models import User

UserSchema = create_schema(User, depth=0)


class UserSchemaManually(Schema):
    id: int
    username: str
    first_name: str
    last_name: str
    password: str
    last_login: datetime
    is_superuser: bool
    email: str
