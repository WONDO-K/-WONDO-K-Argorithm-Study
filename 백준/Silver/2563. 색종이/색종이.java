import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] arr = new int[100][100];
        int n = Integer.parseInt(br.readLine());
        int ans = 0;

        for (int t = 0; t < n; t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            for (int i = a; i < a + 10; i++) {
                for (int j = b; j < b + 10; j++) {
                    if (arr[i][j] == 0) {
                        ans++;
                        arr[i][j] += 1;
                    }
                    
                }
            }
        }

        br.close();
        System.out.println(ans);
    }
}