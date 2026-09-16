
class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] rows = new HashSet[9];
        Set<Character>[] cols = new HashSet[9];
        Set<Character>[] boxes = new HashSet[9];

        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }

        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {

                char num = board[row][col];

                if (num == '.') {
                    continue;
                }

                int box = (row / 3) * 3 + (col / 3);

                if (rows[row].contains(num) ||
                    cols[col].contains(num) ||
                    boxes[box].contains(num)) {
                    return false;
                }

                rows[row].add(num);
                cols[col].add(num);
                boxes[box].add(num);
            }
        }

        return true;
    }
}