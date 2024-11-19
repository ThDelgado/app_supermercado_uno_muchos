from django.shortcuts import render, redirect
from .models import Producto, Fabrica 

from .forms import ProductoFormAdd
from django.contrib import messages


# Create your views here.

           
def listado_productos_view(request):
    contexto = {}
    productos = Producto.objects.all()
    contexto["productos"] = productos    
    return render(request, "inventario/listado_productos.html", contexto)



def add_producto(request):
    contexto = {}
        
    if request.method == 'GET':
        contexto["form"] = ProductoFormAdd()
        return render(request, 'inventario/add_producto.html', contexto)
    
    if request.method == 'POST':   #
        
        form = ProductoFormAdd(request.POST)
        contexto["form"] = form 
        
        print(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, "Producto creado correctamente.")
            return redirect('listado_productos')
            
        else:
            messages.error(request, "Algo ha fallado, revise bien los datos ingresados.")
            return render(request, 'inventario/add_producto.html', contexto)
  