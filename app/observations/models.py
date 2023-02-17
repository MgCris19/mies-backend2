from django.db import models
from app.modelBase.models import ModelBase
from app.entrepreneurShip.models import Entrepreneurship

# Create your models here.
class Observations(ModelBase):
    id = models.AutoField(primary_key=True, db_column='idt_obs_mies')
    detail = models.CharField(
        max_length=45, blank=True, null=True, db_column='detalle')
    entrepreneurship = models.ForeignKey(Entrepreneurship, db_column='id_emprendimiento',
                                         on_delete=models.DO_NOTHING)
    type_observation = models.CharField(
        max_length=45, blank=True, null=True, db_column='tipo_observacion')


    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value   

    class Meta:
        db_table = 'tbl_observaciones'

    def __str__(self):
       return self.detail
