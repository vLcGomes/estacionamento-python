class Estacionamento:

    def __init__(self):

        self.PrecoInicial = 5
        self.PrecoHora = 2
        self.vagas = list()

    def AdicionarVeiculo(self, placa):

        self.vagas.append(placa)

    def RemoverVeiculo(self, placa):

        self.vagas.remove(placa)

    def ListarV(self):
        for vaga in self.vagas:
            print(vaga)

    def Pagamento(self, horas):
        self.valor_total = self.PrecoInicial + (self.PrecoHora * horas)
        print(f'Valor total à Pagar: R${self.valor_total}')
        print(
            'Selecione a Forma de Pagamento\n'
            '1 - Cartão Crédito\n'
            '2 - Cartão Débito\n'
            '3 - PIX\n'
        )
        opcao = int(input())

        if opcao in [1, 2, 3]:
            if opcao == 1:
                print('Insira o cartão no leitor')
                _ = input('Presione o Verde para Confirmar.')
                return False
            elif opcao == 2:
                print('Insira o cartão no leitor')
                _ = input('Presione o Verde para Confirmar.')
                return False
            elif opcao == 3:
                print('QR CODE')
                _ = input('Presione o Verde para Confirmar.')
                return False
        else:
            print('Opção Inválida')
            return True
