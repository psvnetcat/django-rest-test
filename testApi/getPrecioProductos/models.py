from django.db import models

class TableName(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table_name'

    def __str__(self):
        #return 'Asentamiento: {}'.format(self.nombre)
        return self.nombre