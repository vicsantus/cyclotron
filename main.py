from src.cyclotron import cyclotron
import ast


def main():
    particle = input("Digite a particle (n, p ou e): ").lower()
    matrix_str = input("Digite a matrix (Apenas formato NxN): ")

    try:
        matrix = ast.literal_eval(matrix_str)
        if not isinstance(matrix, list) or any(
                not isinstance(row, list) for row in matrix):
            raise ValueError
    except (ValueError, SyntaxError):
        print("Erro: A matriz fornecida não está no formato correto.")
        return

    try:
        print(cyclotron(particle, matrix))
    except Exception:
        print(f'Error: {str(Exception)}')


if __name__ == '__main__':
    main()
