class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        int len = s.length();
        std::set<char> temp;
        for(int i = 0; i < len; i++){
            temp.insert(s[i]);
            for(int j = i + 1; j < len; j++){
                char c = s[j];
                if(temp.find(c) != temp.end())
                    break;
                else
                    temp.insert(c);
            }
            int size = temp.size();
            if(size > ans)
                ans = size; 
            temp.clear();
        }
        return ans;
    }
};
