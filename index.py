import random

def play_guessing_game():
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")
    print("Você consegue adivinhar qual é?")

    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    while not guessed:
        try:
            guess = int(input("Digite o seu palpite: "))
            attempts += 1

            if guess < secret_number:
                print("Muito baixo! Tente novamente.")
            elif guess > secret_number:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {secret_number} em {attempts} tentativas.")
                guessed = True
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    play_guessing_game()
