from django.shortcuts import render, redirect
from .models import Tienda, Boleta, detalle_boleta
from .forms import TiendaForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from PetParadise.compra import Carrito
from django.core.paginator import Paginator
from django.http import Http404
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def tours(request):
    return render(request, 'tours.html')


def contact(request):
    return render(request, 'contact.html')


def tienda(request):
    tiendas = Tienda.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(tiendas, 10)
        tiendas = paginator.page(page)
    except:
        raise Http404

    datos = {
        'entity': tiendas,
        'paginator': paginator
    }
    return render(request, 'tienda.html', datos)


@login_required
def listabd(request):
    tiendas = Tienda.objects.all()
    datos = {'tiendas': tiendas}
    return render(request, 'listabd.html', datos)


@login_required
def crear(request):
    if request.method == "POST":
        tiendaform = TiendaForm(request.POST, request.FILES)
        if tiendaform.is_valid():
            tiendaform.save()
            return redirect('listabd')
    else:
        tiendaform = TiendaForm()
    return render(request, 'crear.html', {'tiendaform': tiendaform})


@login_required
def eliminar(request, id):
    objetoEliminado = Tienda.objects.get(codigo=id)
    objetoEliminado.delete()
    return redirect('listabd')


@login_required
def modificar(request, id):
    objetoModificado = Tienda.objects.get(codigo=id)
    datos = {
        'form': TiendaForm(instance=objetoModificado)
    }
    if request.method == "POST":
        formulario = TiendaForm(data=request.POST, instance=objetoModificado)
        if formulario.is_valid():
            formulario.save()
            return redirect('listabd')
    return render(request, 'modificar.html', datos)


def registrar(request):
    data = {
        'form': RegistroUserForm()
    }
    if request.method == "POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('index')
        data["form"] = formulario
    return render(request, 'registration/registrar.html', data)


def mostrar(request):
    objetos = Tienda.objects.all()
    datos = {'objetos': objetos}
    return render(request, 'mostrar.html', datos)


def agregar_producto(request, id):
    carrito_compra = Carrito(request)
    tienda = Tienda.objects.get(codigo=id)
    carrito_compra.agregar(tienda=tienda)
    return redirect('tienda')


def eliminar_producto(request, id):
    carrito_compra = Carrito(request)
    tienda = Tienda.objects.get(codigo=id)
    carrito_compra.eliminar(tienda=tienda)
    return redirect('tienda')


def restar_producto(request, id):
    carrito_compra = Carrito(request)
    tienda = Tienda.objects.get(codigo=id)
    carrito_compra.restar(tienda=tienda)
    return redirect('tienda')


def limpiar_carrito(request):
    carrito_compra = Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')


@login_required
def generarBoleta(request):
    precio_total = 0
    for key, value in request.session['carrito'].items():
        precio_total = round(precio_total + (int(value['precio']) * 0.19) + int(value['precio']) * int(value['cantidad']) + 3990)
    boleta = Boleta(total=precio_total, estado='PP')  # Estado inicial: 'Procesando Pedido'
    boleta.save()

    productos = []
    for key, value in request.session['carrito'].items():
        producto = Tienda.objects.get(codigo=value['tienda_id'])
        cant = value['cantidad']
        subtotal = cant * int(value['precio'])
        detalle = detalle_boleta(id_boleta=boleta, id_producto=producto, cantidad=cant, subtotal=subtotal)
        detalle.save()
        productos.append(detalle)

        producto.stock -= cant
        producto.save()

    datos = {
        'productos': productos,
        'fecha': boleta.fechaCompra,
        'total': boleta.total,
        'estado': boleta.get_estado_display(),  # Obtener el valor de estado legible para mostrar en la plantilla
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()

    return render(request, 'detallecarrito.html', datos)







