from fastapi import FastAPI

app = FastAPI(title="API de Rações")

banco = {}

@app.get("/racoes")
def listar():
    return banco

@app.get("/racoes/{id}")
def buscar(id:int):
    return banco.get(id, {})

@app.post("/racoes/{id}")
def criar(id:int, dados:dict):
    banco[id] = dados
    return dados

@app.put("/racoes/{id}")
def atualizar(id:int, dados:dict):
    banco[id] = dados
    return dados

@app.delete("/racoes/{id}")
def excluir(id:int):
    banco.pop(id, None)
    return {"mensagem":"excluída"}
