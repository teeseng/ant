#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;

int main()
{
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");

    int g, n, x; 
    fin >> n >> g >> x;

    int result = 1;
    g = g % n;
    while(x > 0)
    {
        if(x % 2 == 1)
        {
            result = (result * g) % n;
        }
        x = x >> 1;
        g = (g * g) % n;
    }

    fout << result << endl;
    return n;
}
