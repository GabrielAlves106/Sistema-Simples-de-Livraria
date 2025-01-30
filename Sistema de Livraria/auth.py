import sqlite3
import sys

banco_usuarios = sqlite3.connect('usuarios.db')

cursor = banco_usuarios.cursor()

#cursor.execute("CREATE TABLE usuarios (IDuser integer primary key autoincrement, NOMEuser text, EMAILuser text, SENHAuser text)")

class Cadastro:
    
    def registrar_usuario(self):
        
        nome = input('Digite seu nome: ')
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        cursor.execute("INSERT INTO usuarios (NOMEuser, EMAILuser, SENHAuser) VALUES (?, ?, ?)", (nome, email, senha))
        banco_usuarios.commit()
        print('Usuário cadastrado com sucesso!')
        
class Login:
    
    def logar_usuario(self):
        
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        cursor.execute("SELECT * FROM usuarios WHERE EMAILuser = ? AND SENHAuser = ?", (email, senha))
        user = cursor.fetchall()
        if user:
            return True
        else:
            print("Usuário não encontrado!")
            return sys.exit()

sistema = Login()
sistema.logar_usuario()