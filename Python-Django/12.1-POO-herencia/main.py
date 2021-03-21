import clases

persona = clases.Persona()
persona.setNombre("Jose")
persona.setApellido("Lascar")
persona.setAltura("160cm")
persona.setEdad("31 años")

print(f"Persona consultada: {persona.getNombre(), persona.getApellido(), persona.getEdad()}")
print(persona.hablar())


informatico = clases.Informatico()
informatico.setNombre("Guru")
informatico.setApellido("Viviano")
print("")
print(informatico.getNombre(), informatico.getApellido())
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.programar())
print(informatico.experiencia)
print("---------------------------")


tecnico = clases.TecnicoRedes()
tecnico.setNombre ("Manolo")
print(f"Obteniendo datos de las classes \n {tecnico.auditarRed, tecnico.getNombre(), tecnico.getLenguajes()}") #Lenguaje no lo obtiene, por que no se ejecuta en esta clase, es de informático, usar Super