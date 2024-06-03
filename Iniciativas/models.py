from django.contrib.auth.models import User
from django.db import models

class PerfilUsuario(models.Model):
    USUARIO_CHOICES = [
        ('Estudiante', 'Estudiante'),
        ('Profesor', 'Profesor'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=USUARIO_CHOICES)

class PropuestaProyecto(models.Model):
    
    TECNOLOGIA = 'Tecnología'
    EDUCACION = 'Educación'
    MEDIO_AMBIENTE = 'Medio Ambiente'
    RECREACION = 'Recreación'
    SOCIAL = 'Social'

    OPCIONES_TEMATICAS = [
        (TECNOLOGIA, 'Tecnología'),
        (EDUCACION, 'Educación'),
        (MEDIO_AMBIENTE, 'Medio Ambiente'),
        (RECREACION, 'Recreación'),
        (SOCIAL, 'Social'),
    ]

    nombre_proyecto = models.CharField(max_length=100)
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, related_name='propuestas_estudiante')
    tema = models.CharField(max_length=100, choices=OPCIONES_TEMATICAS) 
    patrocinado = models.BooleanField(default=False)
    profesor_patrocinador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='propuestas_profesor')
    
    def __str__(self):
        return self.nombre_proyecto


User.propuestas_estudiante = models.ForeignKey(PropuestaProyecto, on_delete=models.CASCADE, null=True, related_name='estudiante_propuestas')
User.propuestas_profesor = models.ForeignKey(PropuestaProyecto, on_delete=models.SET_NULL, null=True, related_name='profesor_propuestas')