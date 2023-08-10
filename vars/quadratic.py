#Compute quadratic formula with given vars🧮

a = int(input("Enter int value a: "))
b = int(input("Enter int value b: "))
c = int(input("Enter int value c: "))

x1 = (-b+((b*b)-(4*a*c))**0.5)/(2*a)
x2 = (-b-((b*b)-(4*a*c))**0.5)/(2*a)

print(x1)
print(x2)