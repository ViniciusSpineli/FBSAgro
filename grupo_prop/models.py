from django.db import models

# Create your models here.

class TabItem(models.Model):
    id_item = models.IntegerField(primary_key=True, db_column='COD_ITEM')
    descricao = models.CharField(max_length=255, db_column='DES_ITEM')
    preco = models.DecimalField(max_digits=10, decimal_places=2, db_column='VLR_CUSTO_MEDIO', null=True, blank=True)


    
    class Meta:
        managed = False  # tabela já existe no banco
        db_table = 'TAB_ITEM'  # nome exato da tabela no Oracle