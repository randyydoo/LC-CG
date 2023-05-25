class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 1)
            return 1;
        std::sort(nums.begin(), nums.end());
        int ans = 0;
        int temp = 1;
       for(int i = 1; i < nums.size(); i++){
           if(nums[i] - nums[i - 1] == 1)
                temp += 1;
            if(temp > ans)
                ans = temp;
            if(nums[i] - nums[i - 1] > 1)
                temp = 1;
       }
       return ans;
    }
};
