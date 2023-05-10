# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import uvicorn
from fastapi import FastAPI 

app=FastAPI()

@app.get('/')
def index():
    return {'message':'Hello, Stranger'}

@app.get('/Welcome')
def get_name(name: str):
    return {'Welcone to Nikhil ':f'{name}'}

if __name__=='__main__':
    uvicorn.run(app,host='127.0.0.1',port=8000)
