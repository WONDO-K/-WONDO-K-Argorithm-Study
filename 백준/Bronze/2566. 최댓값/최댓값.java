import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] arr = new int[9][9];
        int max_v = Integer.MIN_VALUE;
        int row = 0;
        int col = 0;

        for (int i=0;i<9;i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j=0;j<9;j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (max_v < arr[i][j]){
                    max_v = arr[i][j];
                    row = i+1;
                    col = j+1;
                }
            }
        }

    

        br.close();
        System.out.println(max_v);
        System.out.println(row+" "+col);

    }
}