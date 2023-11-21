class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // find row
        // if in range binary search
        int top = 0;
        int l = 0;
        int r = matrix[0].size()-1;
        int bot = matrix.size()-1;

        while(top <= bot){
            int curr_row = (top+bot)/2;
            if(matrix[curr_row][0] > target){
                bot = curr_row-1;
            }
            else if(matrix[curr_row][r] < target){
                top = curr_row+1;
            }
            else{
                break;
            }
        }

        int c_row = (top+bot)/2;
        if (c_row < 0 || c_row >= matrix.size()){
            return false;
        }
        while(l <= r){
            int curr_col = (l+r)/2;
            if(matrix[c_row][curr_col] == target){
                return true;
            }
            else if(matrix[c_row][curr_col] >= target){
                r = curr_col-1;
            }
            else{
                l = curr_col+1;
            }
        }
        return false;
    }
};
