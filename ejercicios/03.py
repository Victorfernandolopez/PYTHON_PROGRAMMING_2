#contar las asusencias de las personas
#lista de asusencias
personas = ["susana","tamara","ana","susana","tomas","ana","analia","alberto"]
ausencias = {n: personas.count(n) for n in personas}
print(ausencias)