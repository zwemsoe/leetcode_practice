#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

//Implementing sieve of Eratosthenes prime counting algo

int countPrimes(int n)
{
    if (n <= 2)
        return 0;
    int count = 0;
    vector<int> p;

    for (int i = 2; i < n; i++)
    {
        if (i != 2)
        {
            if (i % 2)
                p.push_back(i);
            else
                p.push_back(-i);
        }
        else
        {
            p.push_back(i);
        }
    }
    int g = 1;
    for (unsigned int c = 3; c * c < n;)
    {
        for (int j = g + c; j < p.size(); j += c)
        {
            if (p[j] > 0)
            {
                p[j] = -p[j];
            }
        }
        int index = nextPrime(g, p);
        c = p[index];
        g = index;
    }

    for (int k = 0; k < p.size(); k++)
    {
        if (p[k] > 0)
            count++;
    }
    return count;
}

int nextPrime(int n, vector<int> &arr)
{
    int res = arr.size() - 1;
    for (int i = n + 1; i < arr.size(); i++)
    {
        if (arr[i] > 0)
        {
            res = i;
            break;
        }
    }
    return res;
}
