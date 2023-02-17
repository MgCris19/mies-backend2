from django.db import models
from django.contrib.auth.base_user import  BaseUserManager,AbstractBaseUser
from app.modelBase.models import ModelBase
from app.profile.models import Profile


class UsuarioProfileManager(BaseUserManager):
    def create_user(self, email, names, password=None):
        if not email:
            raise ValueError('Usuario debe tener un email')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            names=names,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, names, password):
        user = self.create_user(email, names, password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)

        return user

# Create your models here.
class Usuario(AbstractBaseUser,ModelBase):
    id = models.AutoField(primary_key=True, db_column='id_usuario')
    email = models.CharField(unique=True, max_length=45, blank=True, null=True, db_column='email')
    names = models.CharField(max_length=45, blank=True, null=True, db_column='full_name')
    identify = models.CharField(max_length=45, unique=True, db_column='no_identificacion')
    password = models.CharField(max_length=128, blank=True, null=True, db_column='password')
    
    objects = UsuarioProfileManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['names']

    def get_short_name(self):
        return self.names

    def __str__(self):
        txt = '{0} con Email: {1}'
        return txt.format(self.names, self.email)

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'tbl_usuario'


class UserHasProfile(ModelBase):
    id = models.AutoField(primary_key=True, db_column='id_usuario_has_perfil')
    idUser = models.ForeignKey(Usuario, db_column='id_usuario', on_delete=models.DO_NOTHING)
    idProfile = models.ForeignKey(Profile, db_column='id_perfil', on_delete=models.DO_NOTHING)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        db_table = 'tbl_usuario_has_perfil'
        verbose_name = "UsuarioPerfil"
        verbose_name_plural = "UsuariosPerfiles"

    def __str__(self):
        return self.name