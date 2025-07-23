import java.util.*;
import java.lang.*;
import java.io.*;

class Main {

    static int arr[][];
    static boolean visited[];
    static int n;
    static int m;
    static int v;
    static int cnt;

    static Queue<Integer> que = new ArrayDeque<>();


    public static void BFS(int start){
        visited[start] = true;
        que.offer(start);
        System.out.print(start + " ");

        while (!que.isEmpty()) { //큐가 비지 않는 경우만 동작
            int idx = que.poll();
            
            for (int i=1;i<=n;i++){
                if (arr[idx][i]==1 && visited[i]==false){
                    que.offer(i);
                    visited[i] = true;
                    System.out.print(i + " ");
                }
            }

        }


    }


    public static void DFS(int start) {
        visited[start] = true;
        System.out.print(start + " ");
        
        if (cnt==n){
            return;
        }
        cnt++;
        for(int i=1;i<=n;i++){
            if (arr[start][i]==1 && visited[i]==false){
                DFS(i);
            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v = Integer.parseInt(st.nextToken());
        
        arr = new int[n+1][n+1];
        visited = new boolean[n+1]; // 방문 체크


        for (int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            arr[a][b] = arr[b][a] = 1;
        }

        DFS(v);
        System.out.println();

        visited = new boolean[n + 1]; // BFS를 위해 초기
        BFS(v);

    }   
}