from estacionamento import Estacionamento
import os
from random import randint

ParkStage = Estacionamento()
working = True

while working:

    os.system('cls||clear')
    print(
        'Seja Bem Vindo ao ParkStage!\n'
        '1 - Adicionar Veiculo\n'
        '2 - Remover Veiculo\n'
        '3 - Listar Veiculos\n'
        '4 - Encerrar'
    )
    opcao = int(input('Selecione uma Opção:\n'))

    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            placa = input('Insira a Placa do Veículo: ')
            ParkStage.AdicionarVeiculo(placa)
        elif opcao == 2:
            os.system('cls||clear')
            placa = input('Insira a Placa do Veículo: ')
            debito = ParkStage.Pagamento(randint(1, 10))
            if debito == False:
                print('Ok, Operação Concluída')
                _ = input('Presione ENTER para continuar')
                ParkStage.RemoverVeiculo(placa)
            else:
                print(
                    'A saída do veículo não foi autorizada! Devido a uma falha no Pagamento'
                )
                _ = input('Presione ENTER para Reiniciar')
        elif opcao == 3:
            os.system('cls||clear')
            print('Estes são os veículos estacionados!')
            ParkStage.ListarV()
            _ = input('Presione ENTER para continuar')
        elif opcao == 4:
            print('Ok, Encerrando Sistema!')
            working = False
            os.system('cls||clear')
    else:
        print('Essa não é uma opção válida')
