from source.replace import opensiganteng, orang, penambah, pengali, openfile

data = openfile("tests/static/contohexcel2.xlsx")
harapan = [orang(10,"ato", 0),orang(20,"zaki",162)]


def test_opensiganten2():
    hasil= opensiganteng(data)
    assert harapan == hasil

def test_penambah():
    harapan= 100
    hasil = penambah(90,10)
    assert harapan == hasil

def test_pengali():
    harapan = 100
    hasil = pengali(10,10)
    assert harapan == hasil