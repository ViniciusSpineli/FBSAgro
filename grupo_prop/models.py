from django.db import models

# Create your models here.

class GrupoPropriedade(models.Model):
    cod_grupo_propriedade = models.IntegerField(primary_key=True, db_column='COD_GRUPO_PROPRIEDADE')
    des_grupo_propriedade = models.CharField(max_length=255, db_column='DES_GRUPO_PROPRIEDADE')

    class Meta:
        managed = False  # tabela já existe no banco
        db_table = 'TAB_GRUPO_PROPRIEDADE'  # nome exato da tabela no Oracle

class Usuario(models.Model):
    
    COD_USUARIO = models.CharField(max_length=255, db_column='COD_USUARIO')
    DES_USUARIO = models.CharField(max_length=255, db_column='DES_USUARIO')
    SENHA_USUARIO = models.CharField(max_length=255, db_column='SENHA_USUARIO')
    COD_PESSOA = models.IntegerField(db_column='COD_PESSOA')
    FLG_ADMINISTRADOR = models.CharField(max_length=255, db_column='FLG_ADMINISTRADOR')
    
    class Meta:
        managed = False  # tabela já existe no banco
        db_table = 'TAB_USUARIO'  # nome exato da tabela no Oracle        