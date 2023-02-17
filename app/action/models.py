from django.db import models

from app.modelBase.models import ModelBase


class Action(ModelBase):
    id = models.AutoField(primary_key=True, db_column='id_accion')
    name = models.CharField(unique=True,max_length=45, blank=False,null=False, db_column='nombre')
    descripcion = models.CharField(max_length=150, blank=False,null=False, db_column='descripcion')    

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'tbl_accion'
        verbose_name = "Accion"
        verbose_name_plural = "Acciones"

    def __str__(self):
        return str(self.id)
