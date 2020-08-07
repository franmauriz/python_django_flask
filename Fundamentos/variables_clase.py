class VariableClase:
    variable_clase = "Variable de clase"
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        

var = VariableClase("Variable de instancia")

print(var.variable_instancia)

#VariableClase.variable_clase = "Variable de clase"
print(VariableClase.variable_clase)

var.variable_clase="Variable de clase desde el objeto"
print(var.variable_clase)



