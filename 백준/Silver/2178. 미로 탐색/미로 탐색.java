import java.io.*;
import java.util.*;


public class Main {

    static int dx[] = {0,0,-1,1};
    static int dy[] = {-1,1,0,0};
    static int arr[][],n,m;
    static boolean visited[][];
    static int cnt=0;


    public static void bfs(int x, int y){
        Queue<int []> que = new ArrayDeque<>();

        visited[x][y] = true;
        que.offer(new int[] {x,y});

        while (! que.isEmpty()) {
            int[] now = que.poll();
            int now_x = now[0];
            int now_y = now[1];

            for (int i=0;i<4;i++){
                int nx = now_x+dx[i];
                int ny = now_y+dy[i];

                if (0<=nx && nx<n && 0<=ny && ny<m){ // 범위를 벗어나지 않고
                    if (arr[nx][ny] == 1 && !visited[nx][ny]){ // [nx][ny]가 1이면서 아직 방문하지 않은 곳인 경우
                        que.offer(new int[] { nx, ny });
                        visited[nx][ny] = true;
                        arr[nx][ny] = arr[now_x][now_y]+1; // 이전 위치에서 +1 (현자까지 오는데 몇 칸을 이동했는가?)
                    }
                    
                }
            }
        }
        
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr = new int[n][m];
        visited = new boolean [n][m];

        for (int i=0;i<n;i++){
            String s = br.readLine();
            for (int j=0;j<m;j++){
                arr[i][j] = s.charAt(j) - '0'; // '0' 아스키 값 48 숫자의 아스키 값에서 48빼면 원하는 숫자가 나옴
            }
        }
        
        bfs(0, 0);
        System.out.println(arr[n-1][m-1]);


    }
}