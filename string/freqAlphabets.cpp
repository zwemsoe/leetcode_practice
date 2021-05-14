#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

string freqAlphabets(string s)
{
    vector<int> arr;
    for (int i = 0; i < s.length(); i++)
    {
        if (s[i] == '#')
        {
            if (arr.size() != 0)
            {
                arr.pop_back();
                arr.pop_back();
            }
            if (s[i - 2] == '1')
                arr.push_back(s[i - 2] + s[i - 1] - 87);
            else
                arr.push_back(s[i - 2] + s[i - 1] - 78);
        }
        else
        {
            arr.push_back(s[i] - 48);
        }
    }
    string res = "";
    for (int j = 0; j < arr.size(); j++)
    {
        res += arr[j] + 96;
    }
    return res;
}
