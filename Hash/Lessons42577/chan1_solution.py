#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    unordered_map<string, int> val;
    for (int i =0 ;i<phone_book.size() ;i++){
        val[phone_book[i]]=1;
    }
    for (int i =0 ;i<phone_book.size() ;i++){
        string temp="";
        for (int j=0;j<phone_book[i].length()-1;j++){
            temp+=phone_book[i][j];
            if (val.end()!=val.find(temp)){
                return false;
                
            }
        }
       
    }
    
    
    
    return answer;
}
