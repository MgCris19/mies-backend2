from django.db import models 
from app.entrepreneur.models import Entrepreneur  
from app.modelBase.models import ModelBase
 
#CREATE YOUR MODELS HERE
 
class Perspective(ModelBase):
    name = models.CharField(max_length=200,blank=False,null=False)

    class Meta:
        db_table = 'tbl_perspectiva'

 
class Indicator(ModelBase):
    name = models.CharField(max_length=150,blank=False,null=False)

    class Meta:
        db_table = 'tbl_indicador'
 
class Objective(ModelBase):
    name = models.CharField(max_length=150,blank=False,null=False)
    perspective = models.ForeignKey(Perspective,on_delete=models.CASCADE)
    indicator = models.ForeignKey(Indicator,on_delete=models.CASCADE, unique=True)

    class Meta:
        db_table = 'tbl_objetivo'

 
class Bsc(ModelBase):
    peso = models.IntegerField()
    peso_avance = models.IntegerField()
    peso_alcanzado = models.IntegerField()
    Id_Objetivo = models.ForeignKey(Objective,on_delete=models.CASCADE)
    Id_Indicator = models.ForeignKey(Indicator,on_delete=models.CASCADE,null=True)
    Id_emprendedor = models.ForeignKey(Entrepreneur,on_delete=models.CASCADE, unique=True)
    class Meta:
        db_table = 'tbl_bsc'

