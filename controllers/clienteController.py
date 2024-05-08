import services.database as db;
import models.cliente as cliente
import models.endereco as endereco

def Insere(cliente, endereco):
    db.cursor.execute("INSERT INTO endereco VALUES (%s, %s, %s, %s, %s)", (endereco.id, endereco.rua, endereco.numero, endereco.bairro, endereco.complemento))
    endereco.id = db.cursor.lastrowid

    db.cursor.execute("INSERT INTO cliente VALUES (%s, %s, %s, %s, %s, %s)", (cliente.id, cliente.nome, cliente.cpf, cliente.idade, cliente.telefone, endereco.id))
    db.conexao.commit()

def MostraClientes():
    db.conexao.cmd_reset_connection()
    db.cursor.execute("SELECT * FROM cliente")
    
    clientes = []

    for row in db.cursor.fetchall():
        clientes.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    return clientes
