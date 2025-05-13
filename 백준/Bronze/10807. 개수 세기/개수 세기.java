import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        br.readLine();
        String[] arr = br.readLine().split(" ");

        String v = br.readLine();
        br.close();
        
        int cnt = 0;
        for(String s : arr) if (s.equals(v)) cnt++;
            
        System.out.println(cnt);
    }
}