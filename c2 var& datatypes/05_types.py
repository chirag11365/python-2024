# DATA TYPE CONVERSIONS ...

a =43
t = type(a)  # class <int>
print(t)
# --------------------------------------
b=45.3
t = type(b)  # class <float>
print(t)
# --------------------------------------
c = " chirag"
t = type(c)  # class <str>
print(t)
# -----------------------------------------
d = "45.78"
t = type(d)  # class <str>
print(t) # it will show str not float 
e = float(d) # now it will show float
t = type(e)  # class <float>