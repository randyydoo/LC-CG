class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length() != t.length())
            return false;
       std::map<char, int> sMap;
       for(int i = 0; i < s.length(); i++){
           if(sMap.find(s[i]) != sMap.end())
                sMap[s[i]] += 1;
            else
                sMap.insert(std::make_pair(s[i], 1)); 
            
            if (sMap.find(t[i]) != sMap.end())
                sMap[t[i]] -= 1;
            else
                sMap.insert(std::make_pair(t[i], -1));
       }
       for (const auto& pair : sMap) {
        if (pair.second != 0) 
            return false;
    }
        return true; 

    }
};
//approach 2
class Solution {
public:
    bool isAnagram(string s, string t) {
        std::sort(s.begin(),s.end());
        std::sort(t.begin(), t.end());
        if(s == t)
            return true;
        return false;
    }
};
