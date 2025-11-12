from django.db import models

# Create your models here.

class GrupoPropriedade(models.Model):
    cod_grupo_propriedade = models.IntegerField(primary_key=True, db_column='COD_GRUPO_PROPRIEDADE')
    des_grupo_propriedade = models.CharField(max_length=255, db_column='DES_GRUPO_PROPRIEDADE')
    #preco = models.DecimalField(max_digits=10, decimal_places=2, db_column='VLR_CUSTO_MEDIO', null=True, blank=True)


    
    class Meta:
        managed = False  # tabela já existe no banco
        db_table = 'TAB_GRUPO_PROPRIEDADE'  # nome exato da tabela no Oracle