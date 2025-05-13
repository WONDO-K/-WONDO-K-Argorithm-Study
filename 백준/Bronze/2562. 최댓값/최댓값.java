import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = 9;
        int cnt = 0;
        int num = 0;
        int max_v = Integer.MIN_VALUE;
        int point = 0;
        while (n-- > 0) {
            cnt++;
            num = Integer.parseInt(br.readLine());

            if (max_v<num){
                max_v = num;
                point = cnt;
            }
            
        }

        System.out.println(max_v);
        System.out.println(point);

        br.close();
    }
}