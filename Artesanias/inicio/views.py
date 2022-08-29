
from django.shortcuts import get_object_or_404, render

from .forms import Arte, OpinionForm
from .models import Artesanias, OpinionArtesania
# Create your views here.
def principal(request):
    return render(request,"inicio/principal.html")

def opiniones(request):
    artesanias = OpinionArtesania.objects.all()
    return render(request, "inicio/opiniones.html",{'artesanias': artesanias})

def artesanias(request):
    artesanias = Artesanias.objects.all()
    return render(request, "inicio/artesanias.html",{'artesanias':artesanias})

def registrar(request):
    if request.method == 'POST':
        form = OpinionForm(request.POST)
        if form.is_valid():
            form.save()
            artesanias = OpinionArtesania.objects.all()
            return render(request, 'inicio/opiniones.html', {'artesanias': artesanias})
        form = OpinionForm()
        # Si algo sale mal se reenvia al formulario los datos ingresados
        return render(request, 'inicio/artesanias.html', {'form': form})

def eliminarArtesania(request, id, confirmacion= 'inicio/eliminarArtesania.html'):
    artesania= OpinionArtesania.objects.get(id=id)
    if request.method=='POST':
        artesania.delete()
        artesanias = OpinionArtesania.objects.all()
        return render(request,"inicio/opiniones.html" ,{'artesanias':artesanias},)
    return render(request, confirmacion, {'object':artesania})

def editarArtesania(request, id):
    artesania = get_object_or_404(OpinionArtesania, id=id)
    form = Arte(request.POST, instance=artesania)
    # if form.is_valid():
    form.save()
    artesanias = OpinionArtesania.objects.all()
    return render(request,"inicio/opiniones.html" ,{'artesanias':artesanias})
    # return render(request, 'inicio/editarArtesanias.html', {'artesania':artesania })


def actualizarArtesanias(request,id):
    artesania = OpinionArtesania.objects.get(id=id)
    return render(request, 'inicio/editarArtesanias.html', {'artesania': artesania})