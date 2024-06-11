class Livros:
    
    def __init__ (self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def __str__(self):
        return f'Titulo: {self.titulo}, Autor do livro: {self.autor}, Ano de Publicação: {self.ano_publicacao} '

livro1 = Livros('A Startup Enxuta', 'Eric Ries', 2011)
livro2 = Livros('Use a cabeça: Python', 'Paul Barry', 2019)
print(livro1) 
print(livro2)    

def emprestar_classe(self):
        self.disponivel = False



livro3 = Livros('The para method', 'Tiago Forte', 2023)
print(f'Antes de emprestar o livro: O livro está disponível? {livro3.disponivel}')
livro3.emprestar_classe()

print(f'Depois de emprestar: O livro está disponível? {livro3.disponivel}')


