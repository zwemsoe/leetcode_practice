#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int maximum69Number(int num)
{
    int n = num;
    int pos = 0;
    int x = 0;
    while (n != 0)
    {
        if (n % 10 == 6)
            pos = 3 * pow(10, x);
        x++;
        n /= 10;
    }
    return num + pos;
}

int main()
{
    return 0;
}