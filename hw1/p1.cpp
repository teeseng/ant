#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int x,y;
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");

    fin >> x >> y;
    if((x < 0) || (y < 0))
    {
        return -1;
    }
    else if((x == 0) || (y == 0))
    {
        return 0;
    }

    int r = x % y;
    while(r > 0)
    {
        x = y;
        y = r;  
        r = x % y;
    }
    fout << y << endl;
    return 0;
}
