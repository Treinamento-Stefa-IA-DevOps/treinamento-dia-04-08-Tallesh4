#Talles Henrique De Oliveira Nadiceo
import pickle
from fastapi import FastAPI

app = FastAPI()
@app.post('/model')
## Coloque seu codigo na função abaixo
def titanic(Sex:int, Age:float, Lifeboat:int, Pclass:int):
    with open('model/Titanic.pkl', 'rb') as fid: 
        titanic = pickle.load(fid)
    pred = titanic.predict([[Sex, Age, Lifeboat, Pclass]]).tolist()
    try:
        return {
            'survived': bool(pred[0]),
            'status': 200,
            'message': 'Sucesso  \o' if bool(pred[0]) else 'Morreu',
        }
    except Exception:
        return {
            'message': 'Estou com problemas :('
        }
@app.get('/model')
def get():
    return {'hello':'test'}
