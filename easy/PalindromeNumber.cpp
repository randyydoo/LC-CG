class Solution {
public:
    bool isPalindrome(int x) {
       if(x < 0) {return false;}
       std::string newStr = to_string(x);
       int start = 0;
       int end = newStr.length() - 1;
       while(start <= end){
           if(newStr[start] != newStr[end] ){
               return false;
           }
           start += 1;
           end -= 1;
       }
       return true;
    }
};
