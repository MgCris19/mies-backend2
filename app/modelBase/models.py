from django.db import models

class ModelBase(models.Model):

    id = models.AutoField(primary_key = True)
    state = models.CharField('Estado',max_length =1, default = 'A')
    created_date = models.DateTimeField('Fecha de creación', auto_now = False, auto_now_add = True)
    modified_date = models.DateTimeField('Fecha de modificacion', auto_now = True, auto_now_add = False)
    id_user_created = models.IntegerField('Id usuario creacion', blank = True, null = True)
    id_user_modified = models.IntegerField('Id usario modificacion', blank = True, null = True)

    class Meta:
        abstract = True
        verbose_name = "Modelo Base"
        verbose_name_plural = "Modelos Base"