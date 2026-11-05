n = 100

somma_quad = sum(i**2 for i in range(n+1))
quad_somma = sum(i for i in range(n+1))**2

print(quad_somma - somma_quad)
