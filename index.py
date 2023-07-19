def cyclotron_without_particles(matrix: int):
    for _ in range(matrix):
        print(["1" for _ in range(matrix)])


def accelerate_electron(matrix: int):
    for i in range(4):
        if i == 0:
            print(["e" for _ in range(matrix)])
        else:
            print(["1" for _ in range(matrix - 1)] + ["e"])


def accelerate_proton(matrix: int):
    for i in range(matrix):
        if i == 0:
            print(["p" for _ in range(matrix)])
        elif i == matrix - 1:
            print(["p" for _ in range(matrix - 1)] + ["1"])
        elif i == matrix - 2:
            print(["p"] + ["1" for _ in range(matrix - 3)] + ["p" for _ in range(2)])
        else:
            print(["p"] + ["1" for _ in range(matrix - 2)] + ["p" for _ in range(1)])


def accelerate_neutron(matrix: int):
    for i in range(matrix):
        if i == 0:
            print(["n" for _ in range(matrix)])
        else:
            print(["1" for _ in range(matrix - 1)] + ["1"])


def ciclotron(particula: str, matrix: int):
    if not particula:
        return cyclotron_without_particles(matrix)
    elif particula == "e":
        return accelerate_electron(matrix)
    elif particula == "p":
        return accelerate_proton(matrix)
    elif particula == "n":
        return accelerate_neutron(matrix)
    else:
        print("As únicas partículas aceitas são: e, p, n")


print("WITHOUT PARTICLES")
ciclotron(None, 4)

print()
print("ACCELERATING AN ELECTRON")
ciclotron("e", 4)

print()
print("ACCELERATING A PROTON 4x4")
ciclotron("p", 4)

print()
print("ACCELERATING A PROTON 10x10")
ciclotron("p", 10)  # NxN

print()
print("ACCELERATING A PROTON 6x6")
ciclotron("p", 6)

print()
print("ACCELERATING A NEUTRON")
ciclotron("n", 4)
