import services.database as db;

def verificar_login(profissional): #Verifica se o usuário e a senha estão corretos no banco de dados e returna True se o login for válido, False caso contrário.

  db.cursor.execute("SELECT * FROM profissional WHERE login = %s AND senha = %s", (profissional.login, profissional.senha))
  resultado = db.cursor.fetchone()
  return resultado is not None