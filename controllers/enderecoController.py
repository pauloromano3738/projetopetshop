import services.database as db;
import models.endereco as endereco

def MostraEnderecos():
    db.conexao.cmd_reset_connection()
    db.cursor.execute("SELECT * FROM endereco")
    enderecos = []

    for row in db.cursor.fetchall():
        enderecos.append(endereco.Endereco(row[0], row[1], row[2], row[3], row[4]))
    
    return enderecos

def ExcluiEndereco(endereco_id):
    db.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    db.cursor.execute("DELETE FROM endereco WHERE id_endereco = %s", (endereco_id,))
    db.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    db.conexao.commit()