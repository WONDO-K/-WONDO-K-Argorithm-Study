import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args)  throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //입력
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); // 출력

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();

        for (int i=0;i<n;i++){
            String line = br.readLine(); // 한줄 입력 받기
            StringTokenizer st = new StringTokenizer(line);

            int cmd = Integer.parseInt(st.nextToken());

            if (cmd==1){
                int num = Integer.parseInt(st.nextToken()); // 다음 숫자 가져오기
                stack.push(num);
            } else if (cmd==2){
                if (!stack.isEmpty()) {
                    bw.write(stack.pop() + "\n");
                } else{
                    bw.write("-1\n");
                }
            } else if (cmd==3){
                bw.write(stack.size() + "\n");
            } else if (cmd==4){
                bw.write((stack.isEmpty() ? 1 : 0) + "\n");
            } else if (cmd==5) {
                if (!stack.isEmpty()){
                     bw.write(stack.peek() + "\n");
                } else{
                    bw.write("-1\n");
                }
            }
            
        }
        bw.flush();
        bw.close();
        br.close();
        
    }
}