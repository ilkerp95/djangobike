from django.shortcuts import render
from .models import Gonderi
def gonderi_listesi(request):
    gonderiler = Gonderi.objects.all()
    return render(request, 'blog/gonderi_listesi.html', {'gonderiler': gonderiler})

from django.shortcuts import render
from blogSitesi import models

import pyDes
data = "Ilker Palabiyik"
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)
veri=models.Gonderi(turler=d,icerik=k.decrypt(d))
veri.save()
data = "aaaaaaaaaa"
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)
veri=models.Gonderi(turler=d,icerik=k.decrypt(d))
veri.save()
data = "aaaaabaaaa"
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)
veri=models.Gonderi(turler=d,icerik=k.decrypt(d))
veri.save()
data = "derdimecarebaytarimyok"
k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
d = k.encrypt(data)
veri=models.Gonderi(turler=d,icerik=k.decrypt(d))
veri.save()