import services.database as db;
import models.cliente as cliente

def MostraClientes():
    db.conexao.cmd_reset_connection()
    db.cursor.execute("SELECT * FROM cliente")
    
    clientes = []

    for row in db.cursor.fetchall():
        clientes.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    return clientes

def ExcluiCliente(cliente_id):
    db.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    db.cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (cliente_id,))
    db.cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    db.conexao.commit()
