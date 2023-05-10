# -*- coding: utf-8 -*-
from pydantic import BaseModel

class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float 
    
