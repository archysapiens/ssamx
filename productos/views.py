from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from .forms import UserRegisterForm
from django.contrib import messages


def home(request):
    if request.method == "POST":
        var_email = request.POST.get('id_email')
        var_password = request.POST.get('Password')
        rows = {'row1':'Primer renglon',
               'row2':'Segundo renglon',
               'row3':'Tercero renglon',
               'row4':'Cuarto renglon'}
        num_reg = 0
        try:
            found = Usuario.objects.filter(id_email=var_email, Password=var_password)
            if len(found) > 0:
                num_reg = len(found)
                return render(request, 'productos/producto.html',
                              {'token': var_email, 'password': var_password, 'numreg': num_reg, 'rows':rows})

            else:
                form = UserRegisterForm()
                return render(request, 'productos/debug.html', {'token': var_email,
                                                                'password': var_password, 'numreg': num_reg})
        except Exception as  e:
            #return redirect("/debug")
            return render(request, 'productos/debug.html', {'token': str(e),
                                                                'password': 'except', 'numreg': 'except'})

    else:
        form = UserRegisterForm()
    return render(request, 'productos/home.html', {'form': form})


def debug(request):
    return render(request, 'productos/debug.html')
