import services.database as db;
import models.pet as pet

def Insere(pet):
    db.cursor.execute("INSERT INTO pet VALUES (%s, %s, %s, %s, %s, %s)", (pet.id, pet.nome, pet.idade, pet.peso, pet.raca, pet.cliente_id))
    db.conexao.commit()

def MostraPets():
    db.conexao.cmd_reset_connection()
    db.cursor.execute("SELECT * FROM pet")
    
    pets = []

    for row in db.cursor.fetchall():
        pets.append(pet.Pet(row[0], row[1], row[2], row[3], row[4], row[5]))
    
    return pets
