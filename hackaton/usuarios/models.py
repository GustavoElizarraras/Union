from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db import models
from optimizacion.models import Materia, Licenciatura, Escuela
from aportes.models import Aporte
class Alumno(models.Model):
    """Alumno model.

    Proxy model that extends the base data with other
    information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    materias = models.ForeignKey(Materia, on_delete=CASCADE)
    escuela = models.ForeignKey(Escuela, on_delete=CASCADE)
    licenciatura = models.ForeignKey(Licenciatura, on_delete=CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        """Return username."""
        return self.user.username
