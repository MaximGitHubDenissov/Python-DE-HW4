'''
1. Напишите функцию для транспонирования матрицы

'''
import copy

def matrix_transporn(data: list[list]) -> list[list]:
   result = copy.deepcopy(data)
   for i in range(len(data)):
       for j in range(len(data)):
           result[i][j] = data[j][i]
   return result

matrix = [[1,2,3], [4,5,6], [7,8,9]]

print(matrix_transporn(matrix))