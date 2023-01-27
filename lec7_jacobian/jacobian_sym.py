import sympy as sy

def func(x, y):
    return sy.Matrix([ x**2 + y**2, 2*x + 3*y + 5])

x, y = sy.symbols("x y", real=True)
f = func(x, y)

# Matrix([[x], [y]]) 이나 Matrix([x, y])이나 같다.
z = sy.Matrix([x, y])
z2 = sy.Matrix([[x], [y]])
# print(f"z {z}")
# print(f"z.transpose() {z.transpose()}")
# print(f"z2 {z2}")
# print(f"z2.transpose() {z2.transpose()}")

J = f.jacobian(z)
print(J)

# (1, 2)
J_sym = J.subs([x, 1], [y, 2])
# or 
# J_sym = J.subs([ (x, 1), (y, 2)])

print(J_sym)