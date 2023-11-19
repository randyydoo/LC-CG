class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        map<int,vector<char>> row;
        map<int,vector<char>> col;
        map<int,vector<char>> grid;
        map<int,vector<char>>::iterator it;

        int g = 0;
        for(int i = 0; i < board.size(); i++){
            if (i > 0 && i % 3 == 0) { g += 3; }
            for (int j=0; j < board[i].size(); j++){
                int curr_val = board[i][j];
                int curr_grid = g + (j/3);
                if(curr_val == '.') continue;
                
                it = row.find(i);
                if(it != row.end()){
                    for (char cr: it->second){
                        if(cr == curr_val) return false;
                    }
                }
                it = col.find(j);
                if(it != col.end()){
                    for (char ck: it->second){
                        if(ck == curr_val) return false;
                    }
                }
                it = grid.find(curr_grid);
                if(it != grid.end()){
                    for (char cg: it->second){
                        if(cg == curr_val) return false;
                         
                    }
                }
                row[i].push_back(curr_val);
                col[j].push_back(curr_val);
                grid[curr_grid].push_back(curr_val);
            }
        }
        return true;
    }
};
