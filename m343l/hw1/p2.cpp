#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
    int m, x, y;
    char op;
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
    fin >> m >> op >> x >> y;

    if(op == '*')
    {
        fout << (x * y) % m; 
    }
    else if(op == '+')
    {
        fout << (x + y) % m; 
    }
    return 0;
    
}
