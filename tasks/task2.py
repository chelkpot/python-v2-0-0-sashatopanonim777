# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    x, y, z = map(int, input("введите три числа: ").split())
    
    pencil_price = 3
    pen_price = pencil_price + 2
    marker_price = pen_price + 7
    
    total_cost = x * pencil_price + y * pen_price + z * marker_price
    
    print("ответ:",total_cost)

   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()