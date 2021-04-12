# Importar modulos
from django.http import JsonResponse, HttpResponse 
import pyodbc
import sys

# Importar configuracion de conexion de base de datos
sys.path.append("..")
from db.conexion import conexionSqlServer

# # Configuracion de conexion a base de datos
# server = 'lgalicialap'
# database = 'python'
# username = 'sa'
# password = 'Sql.123'
# conexion = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password
# conexionSqlServer = pyodbc.connect(conexion)

def main(request):
    cursor = conexionSqlServer.cursor()
    cursor.execute("SELECT @@VERSION")
    versionSqlServer = cursor.fetchone()
    app = {
        'mensaje': 'Server API REST - Python/Django is ONLINE',
        'Sql Server Version': versionSqlServer[0]
    }
    return JsonResponse({'server Info': app})
