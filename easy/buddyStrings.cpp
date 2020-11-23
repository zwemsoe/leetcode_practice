#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

bool buddyStrings(string A, string B) {
        if(A.length() != B.length()) 
            return false;
        int index = -1;
        vector<int> v(26);
        for(int i = 0; i< A.length(); i++){
            v[A[i]-97] += 1;
            if(A[i] != B[i]){
                if(index == -1){
                    if(i!=A.length()-1)
                        index = i;
                    else 
                        return false;
                }
                else{
                    char temp = B[i];
                    B[i] = B[index];
                    B[index] = temp;
                    for(int j = 0; j<A.length(); j++){
                        if(A[j]!=B[j])
                            return false;
                    }
                    return true;
                }   
            } 
        }
        for(int k = 0; k<26; k++){
            if(v[k] > 1)
                return true;
        }
        return false;
    }

int main(){
    return 0;
}