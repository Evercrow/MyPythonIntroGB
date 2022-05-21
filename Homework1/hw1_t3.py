# 3. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quart_num = int(input("Enter quart number: "))
quarts = {
    1 : "x € (1,∞) , y € (1,∞)",
    2 : "x € (-1,-∞) , y € (1,∞)",
    3 : "x € (-1,-∞) , y € (-1,-∞)",
    4 : "x € (1,∞) , y € (-1,-∞)",
}
if quart_num in quarts : 
    print(f"{quart_num} -> {quarts[quart_num]}")
else : 
    print(f"You entered incorrect quart number")