from decimal import Decimal
import faust
import json
from faust.types import StreamT
from faustapp.app import app
from .models import Account
from uuid import uuid4
import aiohttp
from faust.web import Request, Response, View


# -----------------------------production code-----------------------------


class AccountRecord(faust.Record):
    name: str
    score: float
    active: bool


topic_addaccount = app.topic('addaccount', value_type=AccountRecord)
topic_disableaccount = app.topic('disableaccount', value_type=AccountRecord)


# define agent consume to topic `addaccount`
@app.agent(topic_addaccount)
async def add_account(accounts: StreamT[AccountRecord]):
    async for account in accounts:
        result = Account.objects.create(
            name=account.name,
            score=Decimal(str(account.score)),
            active=account.active,
        )
        yield result.pk

# define agent consume to topic `disableaccount`
@app.agent(topic_disableaccount)
async def disable_account(account_ids: StreamT[int]):
    async for account_id in account_ids:
        account = Account.objects.get(pk=account_id)
        account.active = False
        account.save()
        yield account.active


# async function do the topic `addaccount` add new record
async def acc_producer(uname, uscore=0.0000000001, uactive=True):
    await topic_addaccount.send(
        value=AccountRecord(name=uname, score=uscore, active=uactive)
    )

# api reponsible to `addaccount` topic data
@app.page('/create_user/')
async def create_user(self, request):
    await acc_producer()
    return self.json({'test produce to topic `addaccount` successful'})


# api reponsible to `addaccount` topic data restful api
@app.page('api/account')
class AccountHandle(View):
    async def get(self, request: Request) -> Response:
        return self.json({"received": "GET", "result": "successful"})

    async def post(self, request: Request) -> Response:
        await acc_producer(uname=request.query['name'])
        return self.json({"received": "POST", "result": "successful", "data": f"{request.query['name']}"})

    async def put(self, request: Request) -> Response:
        return self.json({"received": "PUT", "result": "successful"})

    async def delete(self, request: Request) -> Response:
        return self.json({"received": "DELETE", "result": "successful"})
# -----------------------------end production code-----------------------------


# ----------------------------testing code---------------------------------
class Record(faust.Record):
    value: int


topic = app.topic('concurrency', value_type=Record)


@app.agent(topic, concurrency=200)
async def mytask(records):
    session = aiohttp.ClientSession()
    async for record in records:
        await session.get(f'http://www.google.com/?#q={record.value}')


async def producer():
    for i in range(2):
        await topic.send(value=Record(value=i))

# ----------------------------end testing code---------------------------------