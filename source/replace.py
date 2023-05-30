from attrs import define
from typing import List
import pandas as pd

@define
class orang:
    no:int
    nama:str
    levelkegantengan:str

def openfile(path:str)->List[any]:
    hasil = pd.read_excel(path, header=0).values.tolist()
    return hasil

def opensiganteng(data: list[any])-> List[orang]:
    hasil =[]
    for x in data:
        data= (orang(pengali(x[0],10),x[1],penambah(x[2],12)))
        hasil.append(data)
    return hasil

def pengali(num:int, pengali:int)->int:
    return num*pengali

def penambah(num:int, penambah:int)->int:
    return num+penambah

