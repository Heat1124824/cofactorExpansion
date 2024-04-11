from copy import deepcopy

def submatrix(orig_matrix, row, column): #矩陣降階
    new_matrix = deepcopy(orig_matrix) #將原本的矩陣複製起來，以防止原本矩陣被修改
    new_matrix.remove(orig_matrix[row]) #TODO: 使用remove函式移除矩陣的第一行
    for i in range(len(new_matrix)):
        new_matrix[i].pop(column) #TODO: 使用pop函式移除每一行的第一個數字
    return new_matrix
    
def determinant(matrix):
    num_rows = len(matrix) #矩陣的列數
    #非方陣處理
    for r in matrix:
        if len(r) != num_rows:
            print("不是方陣。")
            return None
    #寫出二階方陣的行列式公式
    if len(matrix) == 2:
        det = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
        return det
    else: #如果輸入方陣不是二階方陣，則進行餘因子展開(cofactor expansion)
        result = 0
        num_cols = num_rows #column數量設為與row數量一樣
        #TODO: 寫一個迴圈讀取第一行所有數字，以第一行進行餘因子展開
        #子矩陣(submatrix)的行列式值也是用determinant函式，這是遞迴寫法
        for j in range(num_cols):
            cofactor = (-1) ** j * matrix[0][j] * determinant(submatrix(matrix, 0, j))
            result += cofactor
        return result
def main():
    test = [[1,2,3,4],
            [5,6,6,5],
            [9,9,11,13],
            [7,10,12,15]]
    answer = determinant(test)
    print(answer)

if __name__ == "__main__":
    main()