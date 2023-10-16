##########  Classe  ##########

class Pessoa:
    def __init__(self, Login, Nome, CPF, Genero, DataNas, Senha):
        self.Login = Login
        self.Nome = Nome
        self.CPF = CPF
        self.Genero = Genero
        self.DataNas = DataNas
        self.Senha = Senha

##########  Lista  ##########

Lista = []


##########  Cadastro  ##########

def CadastroBD(Login, Nome, CPF, Genero, DataNas, Senha):
    obj = Pessoa(Login, Nome, CPF, Genero, DataNas, Senha) #criei o objeto
    Lista.append(obj) #acrescentando o objeto dentro da lista

def AutenticarBD(Login,Senha):
    if not Lista:
        return 'Vazia'
    else:
         for user in Lista:
             if ((user.Login==Login) and (user.Senha==Senha)):
                return 'Certo'
             else:
                return "Errado"

