from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get('/')
async def get_tmp(request:Request):  # async加了就支持异步  把Request赋值给request
    return templates.TemplateResponse('index.html',
                                {'request':request,  # 一定要返回request
                                 'args':'hello world'  # 额外的参数可有可无
                                 }
                                )