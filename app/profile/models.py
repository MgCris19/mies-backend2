from argparse import Action
from django.db import models
from app.menu.models import Screen
from app.action.models import Action

from app.modelBase.models import ModelBase

class Profile(ModelBase):
    id = models.AutoField(primary_key=True, db_column='id_perfil')
    name = models.CharField(unique=True,max_length=45, blank=False,null=False, db_column='nombre')
    descripcion = models.CharField(max_length=150, blank=False,null=False, db_column='descripcion')    

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'tbl_perfil'
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

    def __str__(self):
        return str(self.id)


class PerfilHasScreenHasAction(ModelBase):
    id = models.AutoField(primary_key=True, db_column='id_perfil_has_pantalla_has_accion')
    idProfile = models.ForeignKey(Profile, db_column='id_perfil', on_delete=models.DO_NOTHING)
    idScreen = models.ForeignKey(Screen, db_column='id_pantalla', on_delete=models.DO_NOTHING)
    idAction = models.ForeignKey(Action, db_column='id_accion', on_delete=models.DO_NOTHING)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'tbl_perfil_has_pantalla_has_accion'
        verbose_name = "PerfilPantallaAccion"
        verbose_name_plural = "PerfilesPantallasAcciones"

    def __str__(self):
        return self.name