#include <fstream>
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

// Declaration for Pre-processor
int fast_power(int, int, int);

int main()
{
    ifstream fin;
    ofstream fout;
    ear
        in.open("input.txt");
    fout.open("output.txt", 'w');

    // Find the primitive roots
    int p, e, c;
    vector<int> primitiveRootsList;    
    fin >> e >> c >> p;
    for(int i = 0; i < p; i++)
    {
        int v[p-1];
        memset(v, 0, sizeof(v));
        for(int j = 0; j < p; j++)
        {
            int a = ((int)pow(i,j)) % p;      
            v[a - 1] = 1;
        }
        bool isPrimitiveRoot = true;
        for(int k = 0; k < p - 1; k++)
        {
            if(v[k] != 1)
                isPrimitiveRoot = false;
        }
        if(isPrimitiveRoot)
            primitiveRootsList.push_back(i);
    }

    // TESTING 
    /*
    vector<int>::iterator it;
    for(it = primitiveRootsList.begin(); it != primitiveRootsList.end(); ++it)
    {
        cout << *it << " ";      
    }
    cout << endl;
    */

    vector<int>::iterator it;
    for(it = primitiveRootsList.begin(); it != primitiveRootsList.end(); ++it)
    {
        int res = fast_power(*it,e,p);            
        if(res == (c % p))
            cout << *it << endl;
    }

    fin.close();
    fout.close();
}

int fast_power(int x, int e, int p)
{
    int result = 1;
    x = x % p;
    while(e > 0)
    {
        if(e % 2 == 1)
        {
            result = (result * x) % p;
        }
        e = e >> 1;
        x = (x * x) % p;
    }
    return result;
}
