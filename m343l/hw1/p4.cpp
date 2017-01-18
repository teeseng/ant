#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    string c;   
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("output.txt");
    
    getline(fin, c);
    int alpha[26] = {0}; // lower case alphabets
    int bigAlpha[26] = {0}; // upper case alphabets

    for(int i = 0; i < c.size(); i++)
    {
        if(c[i] >= 'A' && c[i] <= 'Z')
        {
            bigAlpha[c[i] - 'A']++;
        }
        else if(c[i] >= 'a' && c[i] <= 'z')
        {
            alpha[c[i] - 'a']++;
        }
    }

    // finding the most frequent of the characters.
    int max = 0;
    int indx = 0;;
    for(int i = 0; i < 26; i++)
    {
        if(alpha[i] > max)
        {
            max = alpha[i];
            indx = i;
        }
    }
    int k = ('e' - 'a') - indx;

    for(int i = 0; i < c.size(); i++)
    {
        if(c[i] >= 'A' && c[i] <= 'Z')
        {
            c[i] += k;
            if(c[i] > 'Z')
                c[i] = 'A' + (c[i] - 'Z') - 1;
            if(c[i] < 'A')
                c[i] = 'Z' + ('A' - c[i]) - 1;

        }
        else if(c[i] >= 'a' && c[i] <= 'z')
        {
            c[i] += k;
            if(c[i] > 'z')
                c[i] = 'a' + (c[i] - 'z') - 1;
            if(c[i] < 'a')
                c[i] = 'z' + ('a' - c[i]) - 1;
        }
    }
    fout << c << endl;
    return 0;
}
