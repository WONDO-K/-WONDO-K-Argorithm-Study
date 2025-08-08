import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

public class Main {
    static int n,m;
    static int[] parent;

    public static int find(int x){
        while (parent[x]!=x) {
            parent[x] = parent[parent[x]]; // 부모의 부모 대표번호로 초기화
            x = parent[x];
        }
        return x; // 부모를 리턴
    }

    public static void union(int a,int b){

        int ra = find(a);
        int rb = find(b);

        if (ra!=rb){
            parent[rb] = ra;
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        parent = IntStream.rangeClosed(0, n+1).toArray();

        for (int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            int order = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            if (order == 1){
                int new_a = find(a);
                int new_b = find(b); 
                if (new_a == new_b){
                    System.out.println("YES");
                } else{
                    System.out.println("NO");
                }
            } else{
                union(a, b);
            }

        }
    }
    
}