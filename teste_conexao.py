import cx_Oracle as db
import os

# Caminho para o Instant Client
INSTANT_CLIENT_PATH = r"C:\oracle\instantclient_11_2"

try:
    # Inicializa o cliente Oracle (modo thick)
    db.init_oracle_client(lib_dir=INSTANT_CLIENT_PATH)
    print("✅ Oracle Instant Client inicializado com sucesso!")
except Exception as e:
    print("❌ Falha ao inicializar o Oracle Client:", e)
    exit()

try:
    # Tenta conectar ado banco
    connection = db.connect(
        user="BECKER",
        password="FB$13271774!",
        dsn="10.10.4.202:1521/xe"
    )
    print("✅ Conectado com sucesso ao banco de dados Oracle!")
    connection.close()
except Exception as e:
    print("❌ Falha ao conectar ao banco de dados:", e)
