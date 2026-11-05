
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# Inicializa a aplicação FastAPI
app = FastAPI()

# Localiza a pasta principal do projeto
BASE_DIR = Path(__file__).resolve().parent

# Disponibiliza CSS, JavaScript e imagens
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

# Rota principal do site
@app.get("/", response_class=HTMLResponse)
def read_root():
    caminho_html = BASE_DIR / "index.html"

    conteudo = caminho_html.read_text(
        encoding="utf-8"
    )

    return HTMLResponse(content=conteudo)
