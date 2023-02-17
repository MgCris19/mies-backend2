from django.db import models
from app.modelBase.models import ModelBase
from app.entrepreneur.models import Entrepreneur
from app.course.models import Course


class EntrepreneurCourse(ModelBase):
    course = models.ForeignKey(Course, db_column='id_curso', on_delete=models.CASCADE, null=False)
    entrepreneur = models.OneToOneField(Entrepreneur, db_column='id_emprendedor', on_delete=models.CASCADE, null=False)
    observations = models.CharField(max_length=120, blank=True,null=True, db_column='observacion')
    type_observation = models.CharField(max_length=10, blank=True, null=True, db_column='finaliza_curso')
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.course

    class Meta:
        db_table = 'tbl_curso_emprendedor'
        verbose_name = "curso_emprendedor"
        verbose_name_plural = "curso_emprendedor"


