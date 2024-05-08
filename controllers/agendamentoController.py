import services.database as db;
import models.agendamento as agendamento
import models.profissional as profissional
import models.cliente as cliente
import models.pet as pet


def Insere(agendamento, profissional, cliente, pet):
    #db.cursor.execute("SELECT * FROM profissional")
    profissional.id = db.cursor.lastrowid

    #db.cursor.execute("SELECT * FROM cliente")
    cliente.id = db.cursor.lastrowid

    #db.cursor.execute("SELECT * FROM pet")
    pet.id = db.cursor.lastrowid

    db.cursor.execute("INSERT INTO agendamento VALUES (%s, %s, %s, %s, %s, %s)", (agendamento.id, agendamento.status, agendamento.data, profissional.id, cliente.id, pet.id))
    db.conexao.commit()

def MostraAgendamentos():
    db.conexao.cmd_reset_connection()
    db.cursor.execute("SELECT * FROM agendamento")
    
    agendamentos = []

    for row in db.cursor.fetchall():
        agendamentos.append(agendamento.Agendamento(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    return agendamentos
