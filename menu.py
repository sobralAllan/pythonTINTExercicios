from exercicios import Exercicios

class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer  = Exercicios()
        self.num1  = 0
        self.num2  = 0

    def mostrarMenu(self):
        print('\n---- MENU ----\n\n'            +
              'Escolha uma das opções abaixo: ' +
              '\n0. Sair'                       +
              '\n1. Somar'                      +
              '\n2. Subtrair'                   +
              '\n3. Dividir'                    +
              '\n4. Multiplicar'                +
              '\n5. Potência'                   +
              '\n6. Raiz'                       +
              '\n7. Tabuada'                    +
              '\n8. ')

    def coletar(self):
        self.num1 = int(input('Informe o primeiro número: '))
        self.num2 = int(input('Informe o segundo número: '))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()  # Chamando as opções
            self.opcao = int(input('Escolha umas opções acima: '))
            if self.opcao == 0:
                print('Obrigado!!!')
            if self.opcao == 1:
                self.coletar() #Chamando o input por meio do coletar
                print(f'A soma dos números digitados é: {self.exer.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'A subtração dos números digitados é: {self.exer.subtrair(self.num1, self.num2)}')
            elif self.opcao == 3:
                self.coletar()
                print(f'A divisão dos números digitados é: {self.exer.dividir(self.num1, self.num2)}')
            elif self.opcao == 4:
                self.coletar()
                print(f'A multiplicação dos números digitados é: {self.exer.multiplicar(self.num1,self.num2)}')
            elif self.opcao == 5:
                self.coletar()
                print(f'A potência dos números digitados é: {self.exer.potencia(self.num1, self.num2)}')
            elif self.opcao == 6:
                self.coletar()
                print(f'A raiz de {self.num1} é: {self.exer.raiz(self.num1)}')
                print(f'A raiz de {self.num2} é: {self.exer.raiz(self.num2)}')
            elif self.opcao == 7:
                self.coletar()
                print(f'A tabuada de {self.num1} é: {self.exer.tabuada(self.num1)}')
                print(f'A tabuada de {self.num2} é: {self.exer.tabuada(self.num2)}')
        
