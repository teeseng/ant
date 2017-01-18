#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
using namespace std;

long fast_power(int, int, int);

int main()
{
    int p, g, h;
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
    fin >> p >> g >> h;

    // Find n.
    long order;
    for(int i = 2; i < p; i++)
    {
        if((p-1) % i == 0)
        {
            if((fast_power(g, i, p)) == 1L)
            {
                order = (long)i;
                break;
            }
        }
    }
    int n = ceil(sqrt(order));

    // Appending the list (baby list)
    long baby[n];
    for(int i = 0; i < n; i++)
    {
        baby[i] = fast_power(g, i, p);
    }
    int x = 1;

    /* Calculating giant step, finding match */
    long ginv = fast_power(g, p - 2, p); // g modulo inverse
    for(int j = 0; j < n; j++)
    {
        long v1 = (h * fast_power(ginv,j * n, p)) % p;
        int flag = 0;
        for(int i = 0; i < n; i++)
        {
            if(baby[i] == v1)
            {
                flag = 1;
                x = i + (j * n);
                break;
            }
        }
        if(flag)
            break;
    }
    fout << x << endl;
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
