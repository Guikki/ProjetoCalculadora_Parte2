from estado_calculadora import EstadoCalculadora

def soma(estado, valor):
    novo_estado = EstadoCalculadora(
        acumulador = estado.acumulador + valor,
        backup = estado.acumulador, 
        memoria = estado.memoria)
    return novo_estado

def subtracao(estado, valor):
    novo_estado = EstadoCalculadora(
        acumulador = estado.acumulador - valor,
        backup = estado.acumulador, 
        memoria = estado.memoria)
    return novo_estado

def multiplicacao(estado, valor):
    novo_estado = EstadoCalculadora(
        acumulador = estado.acumulador * valor,
        backup = estado.acumulador, 
        memoria = estado.memoria)
    return novo_estado

def divisao(estado, valor):
    try:
        novo_estado = EstadoCalculadora(
            acumulador = estado.acumulador / valor,
            backup = estado.acumulador, 
            memoria = estado.memoria)
    except ZeroDivisionError:    
        print("Não é permitida divisão por zero .")
    return novo_estado

def memoriamr(estado):
    valor = input("Digite um número: ")
    if valor != 'mr':
        valor = float(valor)
    elif valor == 'mr':
        valor = estado.memoria
    return valor
   
def invSin(estado):
    estado = EstadoCalculadora(estado.acumulador * -1, estado.backup, estado.memoria)
    return estado
  
def invNum(estado):
    estado = EstadoCalculadora(1 / estado.acumulador, estado.backup, estado.memoria)
    return estado

def quad(estado):
    estado = EstadoCalculadora(estado.acumulador ** 2, estado.backup, estado.memoria)
    return estado

def raizQuad(estado):
    estado = EstadoCalculadora(estado.acumulador ** 0.5 , estado.backup, estado.memoria)
    return estado
    
def c(estado):
    estado = EstadoCalculadora(estado.acumulador*0, estado.backup*0, estado.memoria)
    return estado

def ce(estado):
    estado = EstadoCalculadora(estado.backup, estado.backup, estado.memoria)
    return estado

def mc(estado):
    estado = EstadoCalculadora(estado.acumulador, estado.backup, estado.memoria*0)
    return estado

def mMais(estado):
    estado = EstadoCalculadora(estado.acumulador, estado.backup, estado.memoria + estado.acumulador)
    return estado
  
def mMenos(estado):
    estado = EstadoCalculadora(estado.acumulador, estado.backup, estado.memoria - estado.acumulador)
    return estado

def ms(estado):
    estado = EstadoCalculadora(estado.acumulador, estado.backup, estado.acumulador)
    return estado
  
def mr(estado):
    estado = EstadoCalculadora(estado.memoria, estado.backup, estado.memoria)
    return estado
