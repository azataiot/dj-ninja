# ninja_demo/sync_endpoints / one.py
# Created by azat at 8.02.2023
from typing import List

from ninja import Router
from ninja_demo.models import One, Two
from ninja_demo.schemas.common import OneSchema, TwoSchema, OneSchemaDeep, TwoSchemaDeep

router = Router()


# =========== Sync ===========
@router.get("/one", response={
    200: List[OneSchema],
})
def get_one_all(request):
    objs = One.objects.all()
    return objs


@router.get("/two", response={
    200: List[TwoSchema]
})
def get_two_all(request):
    objs = Two.objects.all()
    return objs


@router.get("/one/deep", response={
    200: List[OneSchemaDeep]
})
def get_one_deep_all(request):
    objs = One.objects.all()
    return objs


@router.get("/two/deep", response={
    200: List[TwoSchemaDeep]
})
def get_two_deep_all(request):
    objs = Two.objects.all()
    return objs


@router.get("/one/last", response={
    200: OneSchema
})
def get_one_last(request):
    obj = One.objects.last()
    return obj


@router.get("/two/last", response={
    200: TwoSchema
})
def get_two_last(request):
    obj = Two.objects.last()
    return obj


@router.get("/one/first/deep", response={
    200: OneSchemaDeep
})
def get_one_first_deep(request):
    obj = One.objects.first()
    return obj


@router.get("/two/first/deep", response={
    200: TwoSchemaDeep
})
def get_two_first_deep(request):
    obj = Two.objects.first()
    return obj
