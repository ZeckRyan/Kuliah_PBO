# Arbbitrary Argument

# This way the function will receive a tuple of arguments, and can access the items accordingly

def total(*angka):
    return sum(angka)

hasil = total(1,2,3,4,5)

print("total dari ", hasil)