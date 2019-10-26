#x^2+bx+c=0
import math as m 
a = int(input("Ведите значение а: "))

b = int(input("Ведите значение b: "))

c = int(input("Ведите значение c: "))

if a == a and b == b and c == c:
	(d) = b * b - 4 * a *c 

elif a == -a and b == -b and c == -c:
	(d) = -b *(-b) - 4 * (-a) * (-c)


else:
	print("Ошибка!")

print("Дискриминант равен: " + str(d))




if d > 0:
	x1 = (-b + m.sqrt(d))/(a + a)
	print("X равен: " + str(x1))
	
	xtoo = (-b - m.sqrt(d))/(a + a)
	print("X2 равен: " + str(xtoo))	

elif d == 0:
	x = -b/(a + a)

	print("Будет один корень, и он равен: " + str(x))

elif d < 0:
	print("Дискриминант отрицательный и он равен: " + str(d))

else:
	print("Error!!!")
