from unicodedata import category
from django.db import models
from app.modelBase.models import ModelBase

class TrainerCategory(ModelBase):
    name = models.CharField(max_length=70, blank=True, null=True, db_column='nombre')
    description = models.CharField(max_length=120, db_column='descripcion', blank=False, null=False)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'tbl_capacitador_categoria'


class Faculty(ModelBase):
    name = models.CharField(max_length=70, blank=True, null=True, db_column='nombre')
    observation = models.CharField(max_length=120, db_column='observacion', blank=False, null=False)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'tbl_facultad'


class Career(ModelBase):
    name = models.CharField(max_length=70, blank=False, null=False, db_column='nombre')
    observation = models.CharField(max_length=120, blank=True, null=True, db_column='observacion')
    faculty_id = models.ForeignKey(Faculty, db_column='id_facultad', on_delete=models.CASCADE)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'tbl_carrera'

class Student(ModelBase):
    document = models.CharField(max_length=10, blank=True, null=True, db_column='documento_identidad')
    name = models.CharField(max_length=50, blank=True, null=True, db_column='nombres')
    lastname = models.CharField(max_length=50, blank=True, null=True, db_column='apellidos')
    email = models.CharField(max_length=70, blank=True, null=True, db_column='correo')
    telephone = models.CharField(max_length=10, blank=True, null=True, db_column='celular')
    career = models.ForeignKey(Career, db_column='id_carrera', on_delete=models.CASCADE, blank=True, null=True, default=1)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'tbl_estudiante'
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return self.name

class Trainer(ModelBase):
    student_id = models.OneToOneField(Student, on_delete=models.CASCADE, max_length=20, null=True)
    category_trainer = models.ForeignKey(TrainerCategory, on_delete=models.CASCADE, null=True)
    
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    def __str__(self):
        return self.student_id.name + ' ' + self.student_id.lastname

    class Meta:
        db_table = 'tbl_capacitador'
