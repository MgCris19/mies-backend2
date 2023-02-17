from django.db import models

from app.modelBase.models import ModelBase


class Menu(ModelBase):
    id = models.AutoField(primary_key=True, db_column='id_menu')
    name = models.CharField(unique=True,max_length=45, blank=False,null=False, db_column='nombre')
    descripcion = models.CharField(max_length=150, blank=False,null=False, db_column='descripcion')
    icono = models.CharField(max_length=45, blank=True,null=True, db_column='icono')
   

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'tbl_menu'
        verbose_name = "Menu"
        verbose_name_plural = "Menus"

    def __str__(self):
        return str(self.id)

class Screen(ModelBase):
    id = models.AutoField(primary_key=True, db_column='id_pantalla')
    name = models.CharField(unique=True,max_length=45, blank=False,null=False, db_column='nombre')
    descripcion = models.CharField(max_length=150, blank=False,null=False, db_column='descripcion')
    uri = models.CharField(max_length=150, blank=False,null=False, db_column='uri')
    icono = models.CharField(max_length=45, blank=True,null=True, db_column='icono')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'tbl_pantalla'
        verbose_name = "Pantalla"
        verbose_name_plural = "Pantallas"

    def __str__(self):
        return str(self.id)

class MenuHasScreen(ModelBase):
    id = models.AutoField(primary_key=True, db_column='id_menu_has_pantalla')
    idMenu = models.ForeignKey(Menu, db_column='id_menu', on_delete=models.DO_NOTHING)
    idScreen = models.ForeignKey(Screen, db_column='id_pantalla', on_delete=models.DO_NOTHING)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'tbl_menu_has_pantalla'
        verbose_name = "MenuPantalla"
        verbose_name_plural = "MenusPantallas"

    def __str__(self):
        return self.name