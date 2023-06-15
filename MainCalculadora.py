import funcoes
from estado_calculadora import EstadoCalculadora
from funcoes import *

def main():

    try:

        # estado = EstadoCalculadora(acumulador=0, backup=0, memoria=0)
        estado = EstadoCalculadora(0, 0, 0)

        print(f'Estado Inicial: Acumulador: {estado.acumulador}; Backup: {estado.backup}; Memória: {estado.memoria}')

        while True:
            
            operacao = str(input('Digite a operação desejada: ')).lower()

            try: 
                if operacao == '=':
                    estado = EstadoCalculadora(estado.acumulador, estado.acumulador, estado.memoria)
                    break

                elif operacao == '+':
                    valor = memoriamr(estado)
                    estado = soma(estado, valor)
                
                elif operacao == '-':
                    valor = memoriamr(estado)
                    estado = subtracao(estado, valor)
                
                elif operacao == '*':
                    valor = memoriamr(estado)
                    estado = multiplicacao(estado, valor)
                
                elif operacao == '/':
                    valor = memoriamr(estado)
                    estado = divisao(estado, valor)

                elif operacao == '+/-':
                    estado = invSin(estado)
                
                elif operacao == '1/x':
                    estado = invNum(estado)
                
                elif operacao == 'x^2':
                    estado = quad(estado)
                
                elif operacao == 'r2x':
                    estado = raizQuad(estado)

                elif operacao == 'c':
                    estado = c(estado)

                elif operacao == 'ce':
                    estado = ce(estado)

                elif operacao == 'mc':
                    estado = mc(estado)

                elif operacao == 'm+':
                    estado = mMais(estado)
                
                elif operacao == 'm-':
                    estado = mMenos(estado)

                elif operacao == 'ms':
                    estado = ms(estado)
                
                elif operacao == 'mr':
                    estado = invSin(estado)

                else:
                    estado = EstadoCalculadora (float(operacao), estado.backup, estado.memoria)
            
            except ValueError:
                print(f'Comando errado. Tente de novo!')
            except ZeroDivisionError:
                print(f'Você tentou dividir por zero. Tente novamente!')

            print(f'Acumulador: {estado.acumulador}; Backup: {estado.backup}; Memória: {estado.memoria}')

        print(f'Resultado Final: Acumulador: {estado.acumulador}; Backup: {estado.backup}; Memória: {estado.memoria}')

    except KeyboardInterrupt:
        print(f'Resultado Final: Acumulador: {estado.acumulador}; Backup: {estado.backup}; Memória: {estado.memoria}')
        print("O usuario decidiu encerrar o sistema")
        
if __name__=='__main__':
    main()  
