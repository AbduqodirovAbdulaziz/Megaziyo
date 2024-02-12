from django.shortcuts import render, redirect
from .models import *
from .forms import *


def hamma_yonalish(request):
    context = {
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, 'hamma_yonalish.html', context)


def hamma_xona(request):
    context = {
        "xonalar": Xona.objects.all()
    }
    return render(request, 'xonalar.html', context)


def hamma_ustoz(request):
    context = {
        "ustozlar": Ustoz.objects.all()
    }
    return render(request, 'hamma_ustoz.html', context)


def hamma_guruh(request):
    context = {
        "guruhlar": Guruh.objects.all()
    }
    return render(request, 'hamma_guruh.html', context)


def hamma_oquvchi(request):
    context = {
        "oquvchilar": Oquvchi.objects.all()
    }
    return render(request, 'hamma_oquvchi.html', context)


def hamma_tolov(request):
    context = {
        "tolovlar": Tolov.objects.all()
    }
    return render(request, 'hamma_tolov.html', context)


# -----------------------Ma'lumot qo'shish------------
def yonalish_add(request):
    if request.method == "POST":
        Yonalish.objects.create(
            nomi=request.POST["nomi"],
            narx=request.POST["narx"],
        )
        return redirect('/hamma_yonalish/')

    return render(request, 'yonalish_add.html', )


def xona_add(request):
    if request.method == "POST":
        Xona.objects.create(
            raqam=request.POST['raqam'],
            nom=request.POST['nom'],
        )
        return redirect('/hamma_xona/')

    return render(request, 'xona_add.html')


def ustoz_add(request):
    if request.method == "Post":
        Ustoz.objects.create(
            ism=request.POST['ism'],
            familiya=request.POST['familiya'],
            yonalish_id=Yonalish.objects.get(id=request.POST['yonalish']),
            tel_raqam=request.POST['tel_raqam'],
            manzil=request.POST['manzil'],
        )
        return redirect('/hamma_ustoz/')
    context = {
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, 'ustoz_add.html', context)


def guruh_add(request):
    if request.method == "POST":
        data = GuruhForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/hamma_guruh/')

    context = {
        "form": GuruhForm()
    }
    return render(request, 'guruh_add.html', context)
    # if request.method == "POST":
    #     Guruh.objects.create(
    #         nom=request.POST['nom'],
    #         yonalish_id=Yonalish.objects.get(id=request.POST['yonalish']),
    #         tashkil_topgan=request.POST['t_t'],
    #         ustoz_id=Ustoz.objects.get(id=request.POST['ustoz']),
    #         xona_id=request.POST['xona'],
    #         dars_vaqti=request.POST['dars_vaqti'],
    #     )
    # context = {
    #     "yonalishlar": Yonalish.objects.all(),
    #     "ustozlar": Ustoz.objects.all(),
    #     "xonalar": Xona.objects.all(),
    # }
    # return render(request, 'guruh_add.html', context)


# ---forms bilan

def oquvchi_add(request):
    if request.method == "POST":
        data = OquvchiForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/hamma_oquvchi/')
    context = {
        "form": OquvchiForm()
    }
    return render(request, 'oquvchi_add.html', context)


def tolov_add(request):
    if request.method == "POST":
        data = TolovForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('/hamma_tolov/')

    context = {
        "form": TolovForm()
    }
    return render(request, 'tolov_add.html', context)


# -----------------------end--------------------

# ----------------O'chirish---------------------

def yonalish_delete(request, pk):
    Yonalish.objects.get(id=pk).delete()
    return redirect('/hamma_yonalish/')


def xona_delete(request, pk):
    Xona.objects.get(id=pk).delete()
    return redirect('/hamma_xona/')


def ustoz_delete(request, pk):
    Ustoz.objects.get(id=pk).delete()
    return redirect('/hamma_ustoz/')


def guruh_delete(request, pk):
    Guruh.objects.get(id=pk).delete()
    return redirect('/hamma_guruh/')


def oquvchi_delete(request, pk):
    Oquvchi.objects.get(id=pk).delete()
    return redirect('/hamma_oquvchi/')


def tolov_delete(request, pk):
    Tolov.objects.get(id=pk).delete()
    return redirect('/hamma_tolov/')


# -----------------------------------------------

# ---------------------Tahrirlash----------------

def yonalish_edit(request, pk):
    if request.method == "POST":
        yonalish = Yonalish.objects.get(id=pk)
        yonalish.nomi = request.POST['nomi']
        yonalish.narx = request.POST['narx']
        yonalish.save()
        return redirect('/hamma_yonalish/')

    context = {
        "yonalish": Yonalish.objects.get(id=pk)
    }
    return render(request, 'yonalish_edit.html', context)


def xona_edit(request, pk):
    if request.method == "POST":
        xona = Xona.objects.get(id=pk)
        xona.raqam = request.POST['raqam']
        xona.nom = request.POST['nom']
        xona.save()
        return redirect('/hamma_xona/')
    context = {
        "xonalar": Xona.objects.get(id=pk)
    }
    return render(request, 'xona_edit.html', context)


def ustoz_edit(request, pk):
    if request.method == "POST":
        ustoz = Ustoz.objects.get(id=pk)
        ustoz.ism = request.POST['ism']
        ustoz.familiya = request.POST['familya']
        ustoz.yonalish_id = Ustoz.objects.get(id=request.POST['yonalish'])
        ustoz.tel_raqam = request.POST['tel_raqam']
        ustoz.manzil = request.POST['manzil']
    context = {
        "ustozlar": Ustoz.objects.get(id=pk),
        "yonalishlar": Yonalish.objects.all()
    }
    return render(request, 'ustoz_edit.html', context)

def guruh_edit(request,pk):
    if request.method=="POST":
        guruh=Guruh.objects.get(id=pk)
        guruh.nom=request.POST['nom']
        guruh.yonalish_id=Yonalish.objects.get(id=request.POST['yonalish'])
        guruh.tashkil_topgan=request.POST['t_topgan']
        guruh.ustoz_id=Ustoz.objects.get(id=request.POST['ustoz'])
        guruh.xona_id=Xona.objects.get(id=request.POST['xona'])
        guruh.dars_vaqti=request.POST['d_vaqti']
        guruh.save()
        return redirect('/hamma_guruh/')
    context={
        "guruhlar": Guruh.objects.get(id=pk),
        "yonalishlar": Yonalish.objects.all(),
        "Ustoz": Ustoz.objects.all(),
        "xonalar": Xona.objects.all(),

    }
    return render(request,'guruh_edit.html',context)


def oquvchi_edit(request, pk):
    if request.method=="POST":
        oquvchi=Oquvchi.objects.get(id=pk)
        oquvchi.ism=request.POST['ism']
        oquvchi.familya=request.POST['familya']
        oquvchi.tugilgan_sana=request.POST['t_sana']
        oquvchi.guruh_id=Guruh.objects.get(id=request.POST['guruh'])
        oquvchi.tel_raqam=request.POST['tel_raqam']
        oquvchi.manzil=request.POST['manzil']
        oquvchi.save()
        return redirect('/hamma_oquvchi/')
    context={
        "oquvchilar": Oquvchi.objects.get(id=pk),
        "guruhlar": Guruh.objects.all()
    }
    return render(request,'oquvchi_edit.html',context)

def tolov_edit(request,pk):
    if request.method=="POST":
        tolov=Tolov.objects.get(id=pk)
        tolov.summa=request.POST['summa']
        tolov.qarz=request.POST['qarz']
        tolov.chegirma=request.POST['chegirma']
        tolov.save()
        return redirect('/hamma_tolov/')

    context={
        "Tolov": Tolov.objects.get(id=pk)
    }
    return render(request,'tolov_edit.html',context)
# -----------------------------------------------

def batafsil(request):
    return render(request,'Batafsil.html')

def edit_or_delete(request):
    return render(request,'edir_or_delete.html')

def data_add(request):
    return render(request,'data_add.html')
