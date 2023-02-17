from django.db import models
from app.modelBase.models import ModelBase
from app.academic.models import Trainer


class CourseCategory(ModelBase):
    name = models.CharField(max_length=70, blank=True,null=True, db_column='nombre', unique=True)
    description = models.CharField(max_length=120, blank=True, null=True, db_column='descripcion')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'tbl_curso_categoria'


class LocalityCourses(ModelBase):
    name = models.CharField(max_length=70, blank=True,null=True, db_column='nombre', unique=True)
    observations = models.CharField(max_length=120, blank=True, null=True, db_column='observacion')
    address = models.CharField(max_length=120, blank=True, null=True, db_column='direccion')

    @property
    def _history_LocalityCourses(self):
        return self.changed_by

    @_history_LocalityCourses.setter
    def _history_LocalityCourses(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'tbl_curso_localidad'
        verbose_name = "curso_localidad"
        verbose_name_plural = "curso_localidad"

    def __str__(self):
        return self.name


class Course(ModelBase):
    name = models.CharField(max_length=45, blank=False,null=False, db_column='nombre', unique=True)
    description = models.CharField(max_length=45, blank=False, null=False, db_column='descripcion')
    start_date = models.DateField(blank=False, null=False, db_column='fecha_inicio')
    end_date = models.DateField(blank=False, null=False, db_column='fecha_fin')
    duration_hours = models.IntegerField(blank=False, null=False, db_column='duracion_horas')
    category_course = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, max_length=20, null=True)
    location_course = models.ForeignKey(LocalityCourses, on_delete=models.CASCADE, max_length=20, null=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tbl_curso'
# curso capacitador


class CourseTrainer(ModelBase):
    course = models.OneToOneField(Course, db_column='id_curso', on_delete=models.CASCADE, max_length=20, null=False)
    trainer = models.ForeignKey(Trainer, db_column='id_capacitador', on_delete=models.CASCADE, max_length=20, null=False)
    observation = models.CharField(max_length=120, blank=False, null=False, db_column='observacion')

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.course.name + " - " + self.trainer.name

    class Meta:
        db_table = 'tbl_curso_capacitador'
