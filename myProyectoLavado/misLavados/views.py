from django.shortcuts import render
from .models import SliderIndex
from .models import SliderGaleria
from .models import Insumos
from .models import MisionyVision

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_autent
from django.contrib.auth.decorators import login_required, permission_required  
# Create your views here.


def index(request):
    sliders = SliderIndex.objects.all() 
    return render(request,'web/index.html',{'imagenes': sliders})


def misionyvision(request):
    lista = MisionyVision.objects.all()
    return render(request,'web/mision.html',{'lista': lista})

def compra(request):
    return render(request,'web/compra.html')


def galeria(request):
    sliders1 = SliderGaleria.objects.all()
    return render(request,'web/galeria.html',{'imagenes1': sliders1})








@login_required(login_url='/login/')
@permission_required('misLavados.add_insumos',login_url='/login/')
def insumos(request):
    if request.POST:
        nombre = request.POST.get("txtInsumo")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")
        insumo= Insumos(
            nombre=nombre,
            precio=precio,
            descripcion=descripcion,
            stock=stock
        ) 
        insumo.save()
        return render(request,'web/insumos.html',{'msg':'Insumo grabado'})
    return render(request,'web/insumos.html')





@login_required(login_url='/login/')
@permission_required('misLavados.view_insumos',login_url='/login/')
def lista_insumos(request):
    lista = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista})





@login_required(login_url='/login/')
@permission_required('misLavados.view_insumos',login_url='/login/')
@permission_required('misLavados.delete_insumos',login_url='/login/')
def eliminar_insumo(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        insumo.delete()
        msg='El insumo fue eliminado'

    except:
        msg='No se elimino el insumo'
    lista = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista,'msg':msg})
    



@login_required(login_url='/login/')
def buscar(request,id):
    try:
        insumo = Insumos.objects.get(nombre=id)
        return render(request,'web/formulario_insumo_mod.html',{'insumo':insumo})
    except:
        msg='No existe insumo'
    lista = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista})




@login_required(login_url='/login/')
@permission_required('misLavados.view_insumos',login_url='/login/')
@permission_required('misLavados.change_insumos',login_url='/login/')
def modificar(request):
    if request.POST:
        nombre = request.POST.get("txtInsumo")
        precio = request.POST.get("txtPrecio")
        descripcion = request.POST.get("txtDescripcion")
        stock = request.POST.get("txtStock")

        try:
            insumo = Insumos.objects.get(nombre=nombre)
            insumo.precio = precio
            insumo.descripcion = descripcion    
            insumo.stock = stock
            insumo.save()
            msg = 'Insumos Modificados'
        except:
            msg = 'No modifico'
    lista = Insumos.objects.all()
    return render(request,'web/admin_insumos.html',{'lista_insumos':lista,'msg':msg})    


def login(request):
    if request.POST:
        usuario = request.POST.get("txtUsuario")
        password = request.POST.get("txtContrasenia")
        usu = authenticate(request,username=usuario, password=password)
        if usu is not None and usu.is_active:
            login_autent(request,usu)
            sliders = SliderIndex.objects.all() 
            return render(request,'web/index.html',{'imagenes': sliders})
            
        else:
            return render(request,'web/login.html',{'msg':'El usuario no existe o la contraseña es incorrecta'})

    return render(request,'web/login.html')



def cerrar(request):
    logout(request)
    sliders = SliderIndex.objects.all() 
    return render(request,'web/index.html',{'imagenes': sliders})

def mision(request):
    return render(request,'web/mision.html')

def productos(request):
    return render(request,'web/productos.html')


def registro(request):
    if request.POST:
        nombre = request.POST.get("txtNombre")
        apellido = request.POST.get("txtApellido")
        email = request.POST.get("txtEmail")
        usuario = request.POST.get("txtUsuario")
        pass1 = request.POST.get("txtContrasenia")
        pass2 = request.POST.get("txtContrasenia2")

        if pass1!=pass2:
            return render(request,'web/registro.html',{'msg':'claves incorrectas'})

        try:
            usu = User.objects.get(username=usuario)
            return render(request,'web/registro.html',{'msg':'usuario existente'})
        except:
            try:
                usu = User.objects.get(email=email)
                return render(request,'web/registro.html',{'msg': 'email existente '})
            except:
                usu = User()
                usu.first_name = nombre
                usu.last_name = apellido
                usu.email = email
                usu.username = usuario
                usu.set_password(pass1) 
                usu.save()
                usu = authenticate(request,username=usuario, password=pass1)
                login_autent(request,usu)
                return render(request,'web/index.html')
                sliders = SliderIndex.objects.all() 
                return render(request,'web/index.html',{'imagenes': sliders})
    return render(request,'web/registro.html')


def resenias(request):
    return render(request,'web/resenias.html')


def ubicación(request):
    return render(request,'web/ubicación.html')


# end




# formulario

