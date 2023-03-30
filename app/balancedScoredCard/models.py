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
    indicator = models.ForeignKey(Indicator,on_delete=models.CASCADE, unique=False)

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

class Control(ModelBase):
    bsc = models.ForeignKey(Bsc, on_delete=models.CASCADE,unique=False)
    # bsc = models.ForeignKey(Bsc, on_delete=models.CASCADE, unique=True)
    actividad = models.CharField(max_length=150, blank=False, null=False)
    fecha_inicio = models.DateTimeField(auto_now=False, auto_now_add=False)
    fecha_fin = models.DateTimeField(auto_now=False, auto_now_add=False)
    peso_actividad = models.IntegerField()
    avance = models.IntegerField()
    
    class Meta:
        db_table = 'tbl_control'