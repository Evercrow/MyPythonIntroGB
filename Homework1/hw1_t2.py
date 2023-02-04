# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
    
#     *Пример:*
    
#     - x=34; y=-30 -> 4
#     - x=2; y=4-> 1
#     - x=-34; y=-30 -> 3

X_coord = int(input("Enter X coordinate: "))
Y_coord = int(input("Enter Y coordinate: "))

if (X_coord > 0 and Y_coord >0) : print(f"x={X_coord}; y={Y_coord} -> 1")
elif (X_coord < 0 and Y_coord >0) : print(f"x={X_coord}; y={Y_coord} -> 2")
elif (X_coord < 0 and Y_coord <0) : print(f"x={X_coord}; y={Y_coord} -> 3")
elif (X_coord > 0 and Y_coord <0) : print(f"x={X_coord}; y={Y_coord} -> 4")
elif (X_coord == 0 ) : print(f"point({X_coord},{Y_coord}) is on X axis")
else : print(f"point({X_coord},{Y_coord}) is on Y axis")
