# a demo application to store known information in redis cache and see the improvement in performance
from fastapi import FastAPI
import httpx
import redis_toy
import requests
from starlette.responses import StreamingResponse
import io

app = FastAPI()


def get_cat_image(http_code):
    GITHUB_API_URL = f"https://http.cat/{http_code}"
    response = requests.get(GITHUB_API_URL)
    image = response.content
    redis_toy.redis_set(key=http_code, value=image)
    return image

@app.get("/get_cat_image")
def get_stars(http_code):
    cache = redis_toy.redis_get(key=http_code)
    if cache: 
        return StreamingResponse(io.BytesIO(cache), media_type="image/png")
    image = get_cat_image(http_code)
    return StreamingResponse(io.BytesIO(image), media_type="image/png")
    