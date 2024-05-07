import services.database as db;
import models.endereco as endereco

def Insere(endereco):
    db.cursor.execute("INSERT INTO endereço VALUES (%s, %s, %s, %s, %s)", (endereco.id, endereco.rua, endereco.numero, endereco.bairro, endereco.complemento))
    db.conexao.commit()

def MostraEnderecos():
    db.conexao.cmd_reset_connection()
    db.cursor.execute("SELECT * FROM endereço")
    
    enderecos = []

    for row in db.cursor.fetchall():
        enderecos.append(endereco.Endereco(row[0], row[1], row[2], row[3], row[4]))
    
    return enderecos