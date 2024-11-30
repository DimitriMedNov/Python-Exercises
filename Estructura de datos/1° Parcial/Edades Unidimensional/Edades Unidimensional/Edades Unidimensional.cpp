// Edades Unidimensional.cpp
#include <iostream>
using namespace std;
const int Personas = 10;

int main()
{
    char continuar;
    do {
        double Edades[Personas];
        string Person[10] = { "Persona 1: ", "Persona 2: ", "Persona 3: ", "Persona 4: ", "Persona 5:" , "Persona 6: ", "Persona 7: ", "Persona 8: ", "Persona 9: ", "Persona 10: " };
        double suma, promedio, mayor, menor;
        int idxmax, idxmen;

        for (int i = 0; i < Personas; i++)
        {
            suma = 0;
            promedio = 0;
            cout << "Proporcione la edad de la " << Person[i];
            cin >> Edades[i];

            suma += Edades[i];
            promedio = suma / 10;
        }
        cout << "El promedio de edades de las personas es " << promedio << endl;
        cout << "";

        mayor = Edades[0];
        menor = Edades[0];
        idxmax = 0;
        idxmen = 0;

        for (int i = 0; i < Personas; i++) {
            //suma += Edades[i];
            if (Edades[i] > mayor) {
                mayor = Edades[i]++;
                idxmax = i++;
            }
            if (Edades[i] < menor) {
                menor = Edades[i]++;
                idxmen = i++;
            }
        }

        cout << "La persona con mayor edad es "<< Person[idxmax]<<"con: " << mayor << " anios " << endl;
        cout << "La persona con menor edad es "<< Person[idxmen]<<"con: " << menor << " anios " << endl;
        cout << "Desea continuar? s/n ";
        cin >> continuar;
    } while (continuar == 's' || continuar == 'S');
}

