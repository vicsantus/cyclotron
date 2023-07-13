from cyclotron import cyclotron
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
        print("Erro: The array provided is not in the correct format.")
        return

    try:
        print(cyclotron(particle, matrix))
    except Exception as e:
        print(f'{type(e).__name__}: {str(e)}')


if __name__ == '__main__':
    main()
