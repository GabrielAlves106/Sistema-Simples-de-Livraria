import sqlite3
import sys
from utils import CadastroLivros, ConsultaLivros, PesquisarLivros, ApagarLivros
from auth import Cadastro, Login



class Menu:
    
    def __init__(self):
        
        self.sistema_login = Login()
        self.menu_principal()
        
    def menu_principal(self):
        
        while True:
            
            print('1 - Cadastro de livros')
            print('2 - Consulta de livros')
            print('3 - Pesquisa de livros')
            print('4 - Registrar usuário ')
            print('5 - Apagar Livro      ')
            print('6 - Sair')
            
            try:
                
                opcao = int(input('Digite a opção desejada: '))
                    
                if opcao == 1:
                    sistema_cadastro = CadastroLivros()
                    sistema_cadastro.cadastro_livros()
                    
                        
                elif opcao == 2:
                    sistema_consulta = ConsultaLivros()
                    sistema_consulta.consultar_livros()
                    
                        
                elif opcao == 3:
                    sistema_pesquisa = PesquisarLivros()
                    sistema_pesquisa.pesquisar_livros()
                    
                elif opcao == 5:
                    sistema_apagar = ApagarLivros()
                    sistema_apagar.apagar_livros()
                    
                else:
                    print("erro")
                    
            except ValueError:
                print('Digite um número inteiro!')
            
sistema = Menu()


 