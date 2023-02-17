from django.db import models

from app.modelBase.models import ModelBase
from app.entrepreneurShip.models import Entrepreneurship 

# Create your models here.


class TypeActivityEconomic(ModelBase):
    
    name = models.CharField(max_length=70, blank=True,null=True, db_column='nombre', default='')
    description = models.CharField(max_length=120, blank=True, null=True, db_column='descripcion')
    mies_code = models.IntegerField(blank=True, null=True, db_column='codigoMies')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_tipo_actividad_economica'


class EntrepreneurShipActivityEconomic(ModelBase):
    entrepreneurship = models.ForeignKey(Entrepreneurship, on_delete=models.CASCADE, db_column='idEmprendimiento')
    typeActEcon = models.ForeignKey(TypeActivityEconomic, on_delete=models.CASCADE, db_column='idTipoActividadEconomica')
    description = models.CharField(max_length=150, blank=True, null=True, db_column='descripcion')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_emprendimiento_tipo_actividad_economica'
