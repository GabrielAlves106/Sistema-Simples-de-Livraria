import sqlite3

class CadastroLivros:
    
    def cadastro_livros(self):
        
        banco_livros = sqlite3.connect('livros.db')
        
        cursor = banco_livros.cursor()
        
        #cursor.execute("CREATE TABLE livros (IDlivro integer primary key autoincrement, TITULOlivro text, AUTORlivro text, ANOlancamento integer, GENEROlivro text)")
        
        titulo = input('Digite o título do livro: ')
        autor = input('Digite o autor do livro: ')
        ano = int(input('Digite o ano de lançamento do livro: '))
        genero = input('Digite o gênero do livro: ')
        cursor.execute("INSERT INTO livros (TITULOlivro, AUTORlivro, ANOlancamento, GENEROlivro) VALUES (?, ?, ?, ?)", (titulo, autor, ano, genero))
        banco_livros.commit()
        print('Livro cadastrado com sucesso!')
        
class ConsultaLivros:
    
    def consultar_livros(self):
        
        banco_livros = sqlite3.connect('livros.db')
        
        cursor = banco_livros.cursor()
        
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        for livro in livros:
            print(livro)
        
class PesquisarLivros:
    
    def pesquisar_livros(self):
        
        banco_livros = sqlite3.connect('livros.db')     
        
        cursor = banco_livros.cursor()
        
        titulo = input('Digite o título do livro: ')
        cursor.execute("SELECT * FROM livros WHERE TITULOlivro = ?", (titulo,))
        livro = cursor.fetchall()
        if livro:
            print(livro)
        else:
            print('Livro não encontrado!')
            
class ApagarLivros:
    
    def apagar_livros(self):
        
        banco_livros = sqlite3.connect('livros.db')
        
        cursor = banco_livros.cursor()
        
        titulo = input('Digite o título do livro: ')
        cursor.execute("DELETE FROM livros WHERE TITULOlivro = ?", (titulo,))
        banco_livros.commit()
        print('Livro apagado com sucesso!')
            

sistema = ConsultaLivros()
sistema.consultar_livros()