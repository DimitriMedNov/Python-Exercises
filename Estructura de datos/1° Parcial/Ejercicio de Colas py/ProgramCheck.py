import Opciones as op


n = 1
while n == 1:
    print("*******Wselect an option*****")
    print("1.Registrar un paciente")
    print("2.Eliminar alguien atendido")
    print("3.Proximos pacientes")
    print("4.Acabar el programa")
    print(" ")
    
    option = input()
    z = op.Opciones()
    z.numbers_of_options(option)

