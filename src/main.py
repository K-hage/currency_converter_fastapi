from fastapi import FastAPI, HTTPException
from starlette.responses import RedirectResponse
from src.rates import rates_router

app = FastAPI(
    title='Currency Converter',
)

app.include_router(rates_router, prefix='/api')


@app.get("/", include_in_schema=False)
def read_root() -> RedirectResponse:
    return RedirectResponse(url='/docs')


@app.get("/{path:path}", include_in_schema=False)
async def get_any(path: str):
    raise HTTPException(status_code=404, detail='Страница не найдена')
