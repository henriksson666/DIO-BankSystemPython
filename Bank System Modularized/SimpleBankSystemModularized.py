from datetime import date

class User:
    def __init__(self, name, birthdate, cpf, address):
        self.name = name
        self.birthdate = birthdate
        self.cpf = cpf
        self.address = address


class Account:
    account_number = 1

    def __init__(self, user):
        self.agency = "0001"
        self.account_number = Account.account_number
        Account.account_number += 1
        self.user = user
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

    def saque(self, *, valor):
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

    def extrato(self, /, *, include_personal_info=False):
        print("----- Extrato Bancário -----")
        if include_personal_info:
            print(f"Nome: {self.user.name}")
            print(f"Data de Nascimento: {self.user.birthdate}")
            print(f"CPF: {self.user.cpf}")
            print(f"Endereço: {self.user.address}")
        if len(self.depositos) == 0 and len(self.saques) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")


class Banco:
    def __init__(self):
        self.users = []
        self.accounts = []

    def criar_usuario(self, name, birthdate, cpf, address):
        if self._cpf_exists(cpf):
            print("Já existe um usuário com o CPF informado.")
            return None

        user = User(name, birthdate, cpf, address)
        self.users.append(user)
        return user

    def criar_conta_corrente(self, user):
        account = Account(user)
        self.accounts.append(account)
        return account

    def listar_contas(self):
        if len(self.accounts) == 0:
            print("Não há contas cadastradas.")
        else:
            print("----- Lista de Contas -----")
        for account in self.accounts:
            print(f"Agência: {account.agency}")
            print(f"Número da Conta: {account.account_number}")
            print(f"Nome do Cliente: {account.user.name}")
            print("-----------------------------")

    def _cpf_exists(self, cpf):
        for user in self.users:
            if user.cpf == cpf:
                return True
        return False


banco = Banco()

while True:
    print("\nEscolha uma opção:")
    print("1 - Criar Usuário")
    print("2 - Criar Conta Corrente")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Extrato")
    print("6 - Listar Contas")
    print("7 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        name = input("Nome do usuário: ")
        birthdate = input("Data de Nascimento (dd/mm/aaaa): ")
        cpf = input("CPF: ")
        address = input("Endereço: ")
        banco.criar_usuario(name, birthdate, cpf, address)
    elif opcao == "2":
        cpf = input("CPF do usuário: ")
        user = None
        for u in banco.users:
            if u.cpf == cpf:
                user = u
                break
        if user is None:
            print("Não existe um usuário com o CPF informado.")
        else:
            banco.criar_conta_corrente(user)
            print("Conta corrente criada com sucesso.")
    elif opcao == "3":
        account_number = int(input("Número da conta corrente: "))
        account = None
        for a in banco.accounts:
            if a.account_number == account_number:
                account = a
                break
        if account is None:
            print("Não existe uma conta corrente com o número informado.")
        else:
            valor = float(input("Digite o valor a ser depositado: "))
            account.deposito(valor)
    elif opcao == "4":
        account_number = int(input("Número da conta corrente: "))
        account = None
        for a in banco.accounts:
            if a.account_number == account_number:
                account = a
                break
        if account is None:
            print("Não existe uma conta corrente com o número informado.")
        else:
            valor = float(input("Digite o valor a ser sacado: "))
            account.saque(valor=valor)
    elif opcao == "5":
        account_number = int(input("Número da conta corrente: "))
        account = None
        for a in banco.accounts:
            if a.account_number == account_number:
                account = a
                break
        if account is None:
            print("Não existe uma conta corrente com o número informado.")
        else:
            account.extrato(include_personal_info=True)
    elif opcao == "6":
        banco.listar_contas()
    elif opcao == "7":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
