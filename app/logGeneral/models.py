from django.db import models
from app.user.models import Usuario
# Create your models here.
# # migrado
class LogGeneral(models.Model):
    id = models.AutoField(primary_key=True, db_column='id_log_general')
    event = models.DateTimeField(db_column='event_time')
    host = models.TextField(db_column='HOST', )
    mac = models.TextField(db_column='MAC', )
    end_time = models.DateTimeField(blank=True, null=True, db_column='end_time')
    user_data_base = models.CharField(max_length=45, blank=True, null=True, db_column='user_data_base')
    request = models.JSONField(blank=True, null=True, db_column='request')
    sql_text = models.TextField(blank=True, null=True, db_column='sql_text')
    response = models.JSONField(blank=True, null=True, db_column='response')
    user = models.ForeignKey(Usuario, blank=True, null=True, db_column='user', on_delete=models.DO_NOTHING)
    latitude = models.CharField(max_length=45, blank=True, null=True, db_column='latitud')
    length = models.CharField(max_length=45, blank=True, null=True, db_column='longitud')

    class Meta:
        db_table = 'tbl_log_general'