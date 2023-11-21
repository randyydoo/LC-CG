class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int cols = mat.size();
        int ans = 0;
        for(int i = 0; i < cols; i++){
            int len = mat[i].size() - 1;
            //checl if odd num of cols and intersect
            if(cols % 2 != 0 and i == len - i)
                ans += mat[i][len - i];
            else
                ans += mat[i][i] + mat[i][len - i];
        }
        return ans;
    }
};
