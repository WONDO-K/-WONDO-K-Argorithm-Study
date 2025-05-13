import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");
        int min_v = Integer.MAX_VALUE;
        int max_v = Integer.MIN_VALUE;
        int num=0;
        for (int i=0;i<n;i++){
            num = Integer.parseInt(arr[i]);
            if (max_v<num){
                max_v = num;
            }
            if (min_v>num){
                min_v = num;
            }
        }

        System.out.print(min_v+" "+max_v);

            
        br.close();
    }
}