from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def registrar_usuario(request):
    if request.method == 'GET':
        form = userForm()
        contexto = {
            'form':form
        }
    if request.method == 'POST':
        form = userForm(request.POST)
        print(form)
        contexto = {
            'form':form
        }
    if form.is_valid():
        form.save()
        return redirect('perfil')
    return render(request, 'registrar_usuario.html', contexto)

def perfil(request):
    return render(request, 'perfil.html')