import java.util.ArrayDeque;
import java.util.Queue;

class Solution {

    private static final int[] DR = {-1, 1, 0, 0};
    private static final int[] DC = {0, 0, -1, 1};

    public int[] solution(int m, int n, int[][] picture) {
        boolean[][] visited = new boolean[m][n];

        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {

                if (picture[row][col] == 0 || visited[row][col]) {
                    continue;
                }

                numberOfArea++;

                int areaSize = bfs(
                    row,
                    col,
                    picture[row][col],
                    m,
                    n,
                    picture,
                    visited
                );

                maxSizeOfOneArea = Math.max(maxSizeOfOneArea, areaSize);
            }
        }

        return new int[]{numberOfArea, maxSizeOfOneArea};
    }

    private int bfs(
        int startRow,
        int startCol,
        int color,
        int m,
        int n,
        int[][] picture,
        boolean[][] visited
    ) {
        Queue<int[]> queue = new ArrayDeque<>();

        queue.offer(new int[]{startRow, startCol});
        visited[startRow][startCol] = true;

        int areaSize = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();

            int row = current[0];
            int col = current[1];

            areaSize++;

            for (int direction = 0; direction < 4; direction++) {
                int nextRow = row + DR[direction];
                int nextCol = col + DC[direction];

                if (nextRow < 0 || nextRow >= m
                    || nextCol < 0 || nextCol >= n) {
                    continue;
                }

                if (visited[nextRow][nextCol]) {
                    continue;
                }

                if (picture[nextRow][nextCol] != color) {
                    continue;
                }

                visited[nextRow][nextCol] = true;
                queue.offer(new int[]{nextRow, nextCol});
            }
        }

        return areaSize;
    }
}