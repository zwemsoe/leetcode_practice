#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int sumOddLengthSubarrays(vector<int> &arr)
{
    int sum = 0;
    int size = arr.size();
    double times;
    for (int i = 0; i < size; i++)
    {
        times = i * (size - i) + (size - i);
        sum += arr[i] * ceil(times / 2);
    }
    return sum;
}
