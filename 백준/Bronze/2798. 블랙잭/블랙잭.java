import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] arr = Arrays.stream(br.readLine().split(" "))
                        .mapToInt(Integer::parseInt)
                        .toArray();
        
        int max_v = Integer.MIN_VALUE;
        for (int i=0;i<n-2;i++) {
            for (int j=i+1;j<n-1;j++) {
                for (int k=j+1;k<n;k++) {
                    int temp = arr[i]+arr[j]+arr[k];
                    if ((max_v<temp)&&(temp<=m)){
                        max_v = temp;
                    }
                }
            }
        }
        

   

        br.close();
        System.out.println(max_v);
    }
}