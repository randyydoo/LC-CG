class Solution {
public:
    bool isValid(string s) {
       if(s.length() == 1) return false;
       stack<char> stac;

       for(char& c : s){
           if(c == '[' || c == '{' || c == '(')
                 stac.push(c);
           else{
               if(stac.empty()) return false;
           //check if in set
           if(c == '}' && stac.top() =='{')
               stac.pop();
           
           else if(c == ']' && stac.top() == '[')
               stac.pop();
           
           else if(c == ')' && stac.top() == '(')
                stac.pop();
            else
                return false;
           }
        }
        return stac.empty();}
    };
