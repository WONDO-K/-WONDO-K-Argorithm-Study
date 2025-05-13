import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader  br = new BufferedReader (new InputStreamReader(System.in));

        String input = br.readLine();

        StringTokenizer st = new StringTokenizer(input);
        int basket = Integer.parseInt(st.nextToken());
        int cnt = Integer.parseInt(st.nextToken());

        int[] arr = new int[basket];
        
        for (int i=0; i<cnt; i++){
            String input2 = br.readLine();
            st = new StringTokenizer(input2);

            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());

            for (int j=start; j<=end; j++){
                arr[j-1] = num;
            }
            
        }
        StringJoiner sj = new StringJoiner(" ");
        for (int num : arr) {
            sj.add(String.valueOf(num));
        }
        System.out.println(sj);

    }
}