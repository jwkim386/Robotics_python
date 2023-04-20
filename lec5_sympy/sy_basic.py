import sympy as sy

x = sy.symbols('x', real=True)
f0 = x ** 2 + 2 * x + 1
print(f"f0 : {f0}")

df0_fx = sy.diff(f0, x)
print(f"df0_fx : {df0_fx}")

result = df0_fx.subs(x, 1)
print(f"result : {result}")

complex_equ = sy.cos(x)**2 + sy.sin(x)**2
print(f"complex_equ : {complex_equ}")

simple_equ = sy.simplify(complex_equ)
print(f"simple_equ : {simple_equ}")