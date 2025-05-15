import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] arr = new int[n][m];

        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++){
                int temp = Integer.parseInt(st.nextToken());
                arr[i][j] += temp;
            }            
        }

        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++){
                int temp = Integer.parseInt(st.nextToken());
                arr[i][j] += temp;
            }            
        }

        br.close();

        for (int[] row : arr) {
            for (int num : row) {
                System.out.print(num+" ");
            }
            System.out.println();
        }
    }
}