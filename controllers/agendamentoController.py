import services.database as db;
import models.agendamento as agendamento

def Insere(cliente, endereco, pet, agendamento):
    db.cursor.execute("INSERT INTO endereco VALUES (%s, %s, %s, %s, %s)", (endereco.id, endereco.rua, endereco.numero, endereco.bairro, endereco.complemento))
    endereco.id = db.cursor.lastrowid

    db.cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s)", (cliente.id, cliente.nome, cliente.cpf, cliente.idade, cliente.telefone, endereco.id))
    cliente.id = db.cursor.lastrowid

    db.cursor.execute("INSERT INTO pet VALUES (%s, %s, %s, %s, %s, %s)", (pet.id, pet.nome, pet.idade, pet.peso, pet.raca, cliente.id))
    pet.id = db.cursor.lastrowid

    db.cursor.execute("INSERT INTO agendamento VALUES (%s, %s, %s, %s, %s, %s)", (agendamento.id, agendamento.status, agendamento.data, agendamento.profissional_id, cliente.id, pet.id))
    db.conexao.commit()

def MostraAgendamentos():
    db.conexao.cmd_reset_connection()
    db.cursor.execute("SELECT * FROM agendamento")
    
    agendamentos = []

    for row in db.cursor.fetchall():
        agendamentos.append(agendamento.Agendamento(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    return agendamentos

def ExcluiAgendamento(agendamento_id):
    db.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    db.cursor.execute("DELETE FROM agendamento WHERE id_agendamento = %s", (agendamento_id,))
    db.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    db.conexao.commit()