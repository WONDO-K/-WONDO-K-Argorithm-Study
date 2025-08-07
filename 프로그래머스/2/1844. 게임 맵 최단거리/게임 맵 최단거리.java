import java.io.*;
import java.math.*;
import java.util.*;

class Solution { 

    static int[] dx = {0,0,-1,1};
    static int[] dy = {-1,1,0,0};


    public int solution(int[][] maps) {
        ArrayDeque<int[]> que = new ArrayDeque<>();
        int n = maps.length;
        int m = maps[0].length;
        
        que.offer(new int[]{0,0,1});

        while (!que.isEmpty()) {
            int[] arr = que.poll();
            int x = arr[0];
            int y = arr[1];
            int cnt = arr[2];

            if (x==n-1 && y==m-1){
                return cnt;
            }

            for (int i=0;i<4;i++){
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (0<=nx && nx<n && 0<=ny && ny<m){
                    if (maps[nx][ny]==1){
                        maps[nx][ny] = cnt;
                        que.offer(new int[]{nx,ny,cnt+1});
                        maps[nx][ny]=0;
                    }
                }

            }

        }
        return -1;
    }
}