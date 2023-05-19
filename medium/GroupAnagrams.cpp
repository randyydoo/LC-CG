class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
       std::map<std::string, std::vector<std::string>> myMap;       
       std::vector<std::vector<std::string>> ans;
       for(int i = 0; i < strs.size(); i++){
           std::string sortedWord = strs[i];
           std::sort(sortedWord.begin(), sortedWord.end());
           if(myMap.find(sortedWord) != myMap.end())
                myMap[sortedWord].push_back(strs[i]);
           else{
                std::vector<std::string> temp;
                temp.push_back(strs[i]);
                myMap.insert(std::make_pair(sortedWord, temp));
           }
       }
        for (const auto& pair : myMap) {
        const std::vector<std::string> vect = pair.second;
        ans.push_back(vect);
    }
       return ans;
    }
};
