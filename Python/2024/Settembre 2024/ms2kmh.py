def chilometri(v):
    kmh = v*3,6
    return kmh

def metri(v):
    ms = v/3,6
    return ms

v=float(input("Inserire una velocità: "))
kmh = chilometri(v)
ms = metri(v)

print("La velocita' in chilometri orari equivale a:",kmh)
print("La velocita' in metri al secondo equivale a:",ms)