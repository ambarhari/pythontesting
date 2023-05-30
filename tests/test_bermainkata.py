from source.bermainkata import ubahkata, daftarkata

source = "ini hanyalah permainan kata yang tidak biasa, namanya juga kata"
harapan = "ini hanyalah permainan katak yang tidak biasa, namanya juga katak"
harapan2 = "ini hanyalah permainan biasa yang tidak biasa, namanya juga biasa"
mimpi =[["ini",1],
        ["hanyalah",1],
        ["permainan",1],
        ["kata",2],
        ["yang",1],
        ["tidak",1],
        ["biasa",1],
        ["namanya",1],
        ["juga",1]
        ]

def test_permainankata():
    hasil= ubahkata(source, "kata", "katak")
    hasil2= ubahkata(source, "kata", "biasa")

    assert hasil == harapan
    assert hasil2== harapan2

def test_daftarkata():
    hasil= daftarkata(source)

    assert hasil == mimpi
    
