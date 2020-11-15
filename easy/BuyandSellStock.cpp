#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int maxProfit(vector<int> &prices)
{
    if (prices.size() == 0)
    {
        return 0;
    }
    int min = prices[0];
    int max = 0;
    for (int i = 1; i < prices.size(); i++)
    {
        if (prices[i] < min)
        {
            min = prices[i];
        }
        else if (prices[i] - min > max)
        {
            max = prices[i] - min;
        }
    }
    return max;
}

int main()
{
    return 0;
}