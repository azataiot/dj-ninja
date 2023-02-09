# ninja_demo/async_endpoints / one.py
# Created by azat at 8.02.2023
from typing import List

from ninja import Router
from ninja_demo.models import One, Two, User
from ninja_demo.schemas.common import OneSchema, TwoSchema, OneSchemaDeep, TwoSchemaDeep
from ninja_demo.schemas.user import UserSchema, UserSchemaManually

router = Router()


# =========== Async ===========
@router.get("/async/one", response={
    200: List[OneSchema],
})
async def async_get_one_all(request):
    objs = []
    async for each in One.objects.all():
        objs.append(each)
    return objs


@router.get("/async/two", response={
    200: List[TwoSchema]
})
async def async_get_two_all(request):
    objs = []
    async for each in Two.objects.all():
        objs.append(each)
    return objs


@router.get("/async/one/deep", response={
    200: List[OneSchemaDeep]
})
async def async_get_one_deep_all(request):
    objs = []
    async for each in One.objects.select_related().all():
        objs.append(each)
    return objs


@router.get("/async/two/deep", response={
    200: List[TwoSchemaDeep]
})
async def async_get_two_deep_all(request):
    objs = []
    async for each in Two.objects.select_related().all():
        objs.append(each)
    return objs


@router.get("/async/one/last", response={
    200: OneSchema
})
async def async_get_one_last(request):
    obj = await One.objects.alast()
    return obj


@router.get("/async/two/last", response={
    200: TwoSchema
})
async def async_get_two_last(request):
    obj = await Two.objects.alast()
    return obj


@router.get("/async/one/first/deep", response={
    200: OneSchemaDeep
})
async def async_get_one_first_deep(request):
    obj = await One.objects.select_related().afirst()
    return obj


@router.get("/async/two/first/deep", response={
    200: TwoSchemaDeep
})
async def async_get_two_first_deep(request):
    obj = await Two.objects.select_related().afirst()
    return obj


@router.get("/async/users", response={
    200: List[UserSchema]
})
async def async_get_users(request):
    objs = []
    async for each in User.objects.select_related().all():
        objs.append(each)
    first = objs[0]
    print(first)
    print(first.__dict__)
    return objs


@router.get("/async/users/manually", response={
    200: List[UserSchemaManually]
})
async def async_get_users_manually(request):
    objs = []
    async for each in User.objects.select_related().all():
        objs.append(each)
    return objs
