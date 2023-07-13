# Importação de cyclotron e ast
from cyclotron import cyclotron
import ast


def main():
    # Solicita ao usuário que digite a partícula desejada
    particle = input("Digite a particle (n, p ou e): ").lower()

    # Solicita ao usuário que digite a matriz no formato NxN
    matrix_str = input("Digite a matrix (Apenas formato NxN): ")

    try:
        matrix = ast.literal_eval(matrix_str)

        # Verifica se a matriz não está no formato correto
        if not isinstance(matrix, list) or any(
                not isinstance(row, list) for row in matrix):
            raise ValueError
    except (ValueError, SyntaxError):

        # Exibe uma mensagem de erro se a matriz não estiver no formato correto
        print("Erro: The array provided is not in the correct format.")
        return

    try:

        # Chama a função cyclotron com a partícula e a matriz fornecidas
        print(cyclotron(particle, matrix))
    except Exception as e:

        # Exibe o tipo de exceção e a mensagem de erro associada,
        # caso ocorra alguma exceção durante a execução da função
        print(f'{type(e).__name__}: {str(e)}')


if __name__ == '__main__':
    main()
