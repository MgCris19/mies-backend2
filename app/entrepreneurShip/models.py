from django.db import models
from app.modelBase.models import ModelBase
from app.entrepreneur.models import Entrepreneur
from app.academic.models import Student
# Create your models here.

class Entrepreneurship(ModelBase):
    id = models.AutoField(primary_key=True, db_column='id_emprendimiento')
    latitude = models.CharField(max_length=45, blank=True, null=True, db_column='latitud')
    length = models.CharField(max_length=45, blank=True, null=True, db_column='longitud')
    code = models.CharField(max_length=45, blank=True, null=True, db_column='codigo')
    address = models.CharField(max_length=260, blank=True, null=True, db_column='direccion')
    status = models.CharField(max_length=2, blank=True, null=True, db_column='status')
    description = models.CharField(max_length=256, blank=True, null=True, db_column='descripcion')
    entrepreneur = models.ForeignKey(Entrepreneur, db_column='id_emprendedor', on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, db_column='id_estudiante', on_delete=models.DO_NOTHING)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'tbl_emprendimiento'