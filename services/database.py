import mysql.connector

conexao = mysql.connector.connect(
    user='adminprojetopetshop', 
    password='projetopetshop1!', 
    database='petshop', 
    host='projetopetshop.mysql.database.azure.com', 
    ssl_ca='./DigiCertGlobalRootCA.crt.pem'
)

cursor = conexao.cursor()

