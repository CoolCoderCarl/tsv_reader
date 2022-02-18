import pandas
import fastapi

api = fastapi.FastAPI()

signatures_tsv = pandas.read_csv('signatures.tsv', sep='\t')


@api.get("/")
async def status():
    return {"Status": "OK"}


@api.get("/full")
async def full():
    return {"Full": signatures_tsv}


@api.get("/patient/{user_signature}")
async def get_user_signature(user_signature: str, user_id: int):
    return {"user_signature": signatures_tsv[user_signature][user_id]}


@api.get("/signatures/{signatures}")
async def get_signatures(signatures: str):
    return {"signatures": signatures_tsv[signatures]}


# @app.get("/patient/{user_signature}")
# async def get_user_signature(user_signature: str):
#     return {"user_signature": signatures_tsv[user_signature][0]}
