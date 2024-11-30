using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Medina Novelo Jesus D'mitri
namespace Ejercicio_de_Colas
{
    class Program
    {
        static void Main(string[] args)
        {
            int x = 100;
            int[] Pacientes = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 };

            unsafe
            {
                int* p = &x;
                String texto;
                String atencion;

                Console.WriteLine("---------------------------------------------------");
                Console.WriteLine("|              Registro de pacientes               |");
                Console.WriteLine("---------------------------------------------------");
                for (int i = 0; i < Pacientes.Length; i++)
                {
                    fixed (int* v = &Pacientes[i])
                    {
                        Console.WriteLine("Paciente Numero " + *v + " introduzca su nombre del mismo: ");
                        texto = Console.ReadLine();
                        Console.WriteLine("");
                    }
                }
                Console.WriteLine("---------------------------------------------------");
                Console.WriteLine("|               Atencion a pacientes               |");
                Console.WriteLine("---------------------------------------------------");
                for (int c = 0; c < Pacientes.Length; c++)
                {
                    Console.WriteLine("Paciente numero " + Pacientes[c]);
                    Console.WriteLine("Introduzca todo lo que le pasa al paciente: " );
                    atencion = Console.ReadLine();
                    Console.WriteLine("");
                }
            }
        }
    }
}