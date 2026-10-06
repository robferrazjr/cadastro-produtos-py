from classes.AbstractCrud import AbsctractCrud

class Categoria(AbsctractCrud):
    
    arquivo = "db/categorias.json"
    
    def __init__(self, nome):
        self.nome = nome
