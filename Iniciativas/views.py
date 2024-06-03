from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, PropuestaProyectoForm
from .models import PropuestaProyecto

def home(request):
    # Obtener el tema seleccionado, si existe
    tema_filter = request.GET.get('tema', None)

    # Obtener todos los proyectos
    proyectos = PropuestaProyecto.objects.all()

    # Filtrar por tema si se proporciona uno
    if tema_filter:
        proyectos = proyectos.filter(tema=tema_filter)

    # Renderizar el formulario de inicio de sesión
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()

    context = {'form': form, 'proyectos': proyectos, 'user': request.user}
    return render(request, 'index.html', context)

@login_required
def nueva_propuesta(request):
    if request.method == 'POST':
        form = PropuestaProyectoForm(request.POST)
        if form.is_valid():
            propuesta = form.save(commit=False)
            propuesta.estudiante = request.user
            propuesta.save()
            return redirect('home')
    else:
        form = PropuestaProyectoForm()
    return render(request, 'nueva_propuesta.html', {'form': form})

@login_required
def patrocinar_proyecto(request, pk):
    proyecto = get_object_or_404(PropuestaProyecto, pk=pk)
    if request.method == 'POST':
        proyecto.patrocinado = True
        proyecto.profesor_patrocinador = request.user
        proyecto.save()
        return redirect('home')
    return render(request, 'patrocinar_proyecto.html', {'proyecto': proyecto})