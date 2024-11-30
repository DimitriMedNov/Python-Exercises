import Queue as q
import sys

class Switcher(object):

    def numbers_of_options(self, argument):
        """Dispatch method"""
        method_name = "option_" + str(argument)
        # Get the method from 'self'. Default to a lambda.
        method = getattr(self, method_name, lambda: "Invalid Option")
        # Call the method as we return it
        print(method())
 
    def option_1(self):
        print ("Type your name please")
        op= input()
        z = q.Queue()
        z.enqueue(op)
    def option_2(self):
        z = q.Queue()
        z.dequeue()
 
    def option_3(self):
        z = q.Queue()
        z.isEmpty()
    
    def option_4(self):
        z = q.Queue()
        z.size()
    
    def option_5(self):
        z = q.Queue()
        z.scope()
    
    def option_6(self):
        sys.exit("Thank you, good bye!")
   