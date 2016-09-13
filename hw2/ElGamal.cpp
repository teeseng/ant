#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

long fast_power(int base, int x, int n);

int main()
{
    int p, g, m, ga;
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
    fin >> p >> g >> m >> ga;

    //int k = rand() % p;
    //TODO chance line 19 to 17!!
    int k = 197;
    long c1 = fast_power(g, k, p);
    long c2 = (m * fast_power(ga, k, p)) % p;

    fout << c1 << " " << c2 << endl;
    return 0;
}

long fast_power(int g, int x, int n)
{
    long result = 1L;
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
    return result;
}
