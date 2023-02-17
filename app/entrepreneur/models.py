from django.db import models
from app.modelBase.choices import TypeIdentify
from app.modelBase.models import ModelBase
from app.user.models import Usuario
from app.course.models import Course

class AssociationEntrepreneur(ModelBase):
    name = models.CharField(max_length=70, blank=True, null=True, db_column='nombre')
    observation = models.CharField(max_length=120, blank=True, null=True, db_column='observacion')
    

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    def __str__(self):
        return self.identify

    class Meta:
        db_table = 'tbl_asociacion_emprendedor'

class Entrepreneur(ModelBase):
    code = models.CharField(max_length=45, blank=True, null=True, unique=True, db_column='codigo_mies')
    identify = models.CharField(max_length=45, blank=True, null=True, unique=True, db_column='identificacion')
    type_identify = models.CharField(max_length=45, choices=TypeIdentify, blank=True, null=True, db_column='tipo_identificacion')
    entrepreneur = models.CharField(max_length=150, blank=True, null=True, db_column='emprendedor')
    barrio = models.CharField(max_length=45, blank=True, null=True, db_column='barrio')
    sector = models.CharField(max_length=45, blank=True, null=True, db_column='sector')
    address = models.CharField(max_length=260, blank=True, null=True, db_column='domicilio')
    user = models.ForeignKey(Usuario, db_column='id_usuario', on_delete=models.DO_NOTHING)
    association = models.ForeignKey(AssociationEntrepreneur, db_column='id_asociacion', on_delete=models.CASCADE, default=1)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    def __str__(self):
        return self.identify

    class Meta:
        db_table = 'tbl_emprendedor'


class PhoneType(ModelBase):
    description = models.CharField(max_length=45, blank=True, null=True, db_column='descripcion')
    

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    def __str__(self):
        return self.identify

    class Meta:
        db_table = 'tbl_tipo_telefono' 

class PhoneEntrepreneur(ModelBase):
    entrepreneur = models.ForeignKey(Entrepreneur, db_column='idEmprendedor', on_delete=models.CASCADE)
    type_phone = models.ForeignKey(PhoneType, db_column='idTipoTelefono', on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True, db_column='numero')
    

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    def __str__(self):
        return self.entrepreneur

    class Meta:
        db_table = 'tbl_emprendedor_telefono'