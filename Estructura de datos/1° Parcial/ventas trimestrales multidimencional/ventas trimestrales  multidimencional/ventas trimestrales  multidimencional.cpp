#include <iostream>
#include <string>
using namespace std;

//const int PROF = 3, FILAS = 4, COLUMNAS = 4;
// i j k



int main()
{
	float multi[3][4][3] = {};
	for (int i = 0; i < 3; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 3; k++)
			{
				cout << "Proporcione las ventas: ";
				cin >> multi[0][0][0];

				cout << "Proporcione las ventas: ";
				cin >> multi[1][1][1];
			}
		}
	}
}

