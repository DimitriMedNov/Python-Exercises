import Program as p
import sys
#import Program as p

#class Opciones
class Opciones(object):

    def numbers_of_options(self, argument):
        """Dispatch method"""
        method_name = "option_" + str(argument)
        method = getattr(self, method_name, lambda: "Invalid Option")

        print(method())
 
    def option_1(self):
        print ("Escriba el nombre del paciente")
        op= input()
        z = p.Program()
        z.enqueue(op)
        
    def option_2(self):
        z = p.Program()
        z.dequeue()
    
    def option_3(self):
        z = p.Program()
        z.scope()
    
    def option_4(self):
        sys.exit("------------Fin del programa--------------")
    