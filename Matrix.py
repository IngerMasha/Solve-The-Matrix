def make_matrix(matrix):
    symbols = list(matrix)
    rows = int(len(symbols)/3)
    new_matrix=[]
    for i in range(rows):
        row = symbols[i * 3: (i + 1) * 3]
        new_matrix.append(row)
    return new_matrix
def sicret(matrix):
    result = ''
    for i in range(0,3):
        for j in range(0,len(matrix)):
            simbol = matrix[j][i]
            if simbol.isalpha():
                result+=simbol
            else:
                result += ' '
    result=result.split()
    result=' '.join(result)
    return result
def main():
    my_matrix = "7iiTsxh%?i #sM $a #t%^r!"
    new_matrix=make_matrix(my_matrix)
    print(my_matrix)
    print(sicret(new_matrix))

if __name__ == "__main__":
    main()