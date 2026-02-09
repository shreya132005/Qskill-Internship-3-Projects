import numpy as np

def inp_mat(prompt):
    print(prompt)
    rows = int(input("Enter the number of rows: "))

    cols = int(input("Enter the number of cols: "))
    print("Enter the values of matrix row by row: ")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        if len(row) != cols:
            print("Number of columns must match the input")
            return None
        matrix.append(row)
    return np.array(matrix)

def operations():
    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. exit")
        choice = input("Enter your operation(1-4): ")
        if choice == "4":
            break

        mat1 = inp_mat("Matrix 1: ")
        mat2 = inp_mat("Matrix 2: ")
        if choice == "1":
            if mat1.shape == mat2.shape:
                print("Result: \n", mat1+mat2)
            else:
                print("Matrix must have the same dimension")
        elif choice == "2":
            if mat1.shape == mat2.shape:
                print("Result: \n", mat1-mat2)
            else:
                print("Matrix must have the same dimension")
        elif choice == "3":
            if mat1.shape[1] == mat2.shape[0]:
                print("Result: \n", np.dot(mat1,mat2))
            else:
                print("Matrix 1 columns must same the number of row in matrix 2 for multiplication")
        else:
            print("Invalid")

if __name__ == "__main__":
    operations()


