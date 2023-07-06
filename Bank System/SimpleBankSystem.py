from datetime import date

class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.depositos = []
        self.saques = []
        self.num_saques_dia = 0
        self.data_atual = date.today()

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def saque(self, valor):
        if self.saldo >= valor and valor <= 500.0:
            if self.num_saques_dia < 3 and self.data_atual == date.today():
                self.saldo -= valor
                self.saques.append(valor)
                self.num_saques_dia += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            elif self.num_saques_dia >= 3:
                print("Limite máximo de saques diários atingido.")
            else:
                print("O número máximo de saques diários foi reiniciado.")
                self.saldo -= valor
                self.saques.append(valor)
                self.num_saques_dia = 1
        elif self.saldo < valor:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor do saque deve ser menor ou igual a R$ 500.00.")

    def extrato(self):
        print("----- Extrato Bancário -----")
        if len(self.depositos) == 0 and len(self.saques) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")


banco = Banco()

while True:
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        banco.deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        banco.saque(valor)
    elif opcao == "3":
        banco.extrato()
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")