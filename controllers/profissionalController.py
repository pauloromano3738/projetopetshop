import services.database as db;
import models.profissional as profissional

def Insere(profissional):
    db.cursor.execute("INSERT INTO profissional VALUES (%s, %s, %s, %s, %s, %s)", (profissional.id, profissional.nome, profissional.cpf, profissional.ocupacao, profissional.login, profissional.senha))
    db.conexao.commit()

def MostraProfissionais():
    db.conexao.cmd_reset_connection()
    db.cursor.execute("SELECT * FROM profissional")
    

    profissionais = []

    for row in db.cursor.fetchall():
        profissionais.append(profissional.Profissional(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    return profissionais
