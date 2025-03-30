from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import uvicorn

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carregar dados das operadoras
def load_operadoras():
    try:
        return pd.read_csv('data/operadoras_ativas.csv', sep=';', encoding='utf-8')
    except Exception as e:
        print(f"Erro ao carregar arquivo: {e}")
        return pd.DataFrame()

@app.get("/api/operadoras/busca")
async def buscar_operadoras(q: str = Query(None, min_length=2)):
    if not q:
        return {"operadoras": []}
    
    df = load_operadoras()
    
    # Realizar busca em várias colunas
    mask = df['razao_social'].str.contains(q, case=False, na=False) | \
           df['nome_fantasia'].str.contains(q, case=False, na=False) | \
           df['registro_ans'].str.contains(q, case=False, na=False)
    
    resultados = df[mask].head(10).to_dict('records')
    return {"operadoras": resultados}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)