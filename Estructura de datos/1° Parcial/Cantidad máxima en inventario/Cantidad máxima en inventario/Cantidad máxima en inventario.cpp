#include <iostream>
#include <cmath>
#include <conio.h>

using namespace std;
const int NumMeses = 12;

int main()
{
    string Meses[NumMeses] = { "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre" };
    double Ventas[NumMeses], suma, promedio;
    float varianza = 0, desv = 0;
    suma = 0;
    promedio = 0;
    
    for (int i = 0; i < NumMeses; i++) {
        cout << "Proporcione las ventas de " << Meses[i] << ": ";
        cin >> Ventas[i];
        suma += Ventas[i];
    }
    promedio = suma / NumMeses;

    for (int i = 0; i < NumMeses; i++)
    {
        varianza = varianza + pow((Ventas[i] - promedio), 2);
    }

    desv = sqrt(varianza / (NumMeses - 1));

    cout << "El promedio de ventas es: " << promedio << endl;
    cout << "La varianza es: " << varianza << endl;
    cout << "La desviacion estandar es: " << desv << endl;
}
