from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI(
    title="REST API для конвертации температуры",
    description="Сервис для перевода температуры из Цельсия в Фаренгейт и наоборот",
    version="1.0.0"
)

@app.get("/to_celsius")
def to_celsius(fahrenheit: float = Query(..., description="Температура в градусах Фаренгейта")):
    celsius = (fahrenheit - 32) * 5 / 9
    return JSONResponse(content={"фаренгейт": fahrenheit, "цельсий": round(celsius, 2)})

@app.get("/to_fahrenheit")
def to_fahrenheit(celsius: float = Query(..., description="Температура в градусах Цельсия")):
    fahrenheit = celsius * 9 / 5 + 32
    return JSONResponse(content={"цельсий": celsius, "фаренгейт": round(fahrenheit, 2)})
