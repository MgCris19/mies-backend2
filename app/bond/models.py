from calendar import month
from datetime import datetime, timedelta
from pickle import TRUE
from re import S
from django.db import models
from app.entrepreneur.models import Entrepreneur
from app.modelBase.models import ModelBase

# Create your models here.


class Bond(ModelBase):
    value = models.FloatField(blank=True, null=True, db_column='valor')
    description = models.CharField(max_length=45, blank=True, null=True, db_column='descripcion')
    entrepreneur = models.ForeignKey(Entrepreneur, db_column='id_emprendedor', on_delete=models.CASCADE)
    date_init = models.DateTimeField(blank=True, null=True, db_column='fecha_inicio_cdh',  auto_now=False, auto_now_add=True)
    date_end = models.DateTimeField(blank=True, null=True, db_column='fecha_fin_cdh', auto_now=False, auto_now_add=False)
    month_plazo = models.IntegerField(db_column='meses_plazo', default=1)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.date_end = datetime.now() +timedelta(days=self.month_plazo*30)
        print('inicio: ',self.date_end)
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'tbl_bono'

    