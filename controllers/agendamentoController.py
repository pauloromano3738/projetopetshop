import services.database as db;
import models.cliente as cliente
import models.endereco as endereco
import models.pet as pet
import models.agendamento as agendamento
import models.profissional as profissional


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
