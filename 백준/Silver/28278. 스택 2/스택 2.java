import java.util.*;
import java.io.*;

class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out)); 

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();

        while (n-- > 0) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int cmd = Integer.parseInt(st.nextToken());

            switch (cmd) {
                case 1:
                    stack.push(Integer.parseInt(st.nextToken()));
                    break;
                case 2:
                    bw.write((stack.isEmpty() ? -1 : stack.pop()) + "\n");
                    break;
                case 3:
                    bw.write(stack.size() + "\n");
                    break;
                case 4:
                    bw.write((stack.isEmpty() ? 1 : 0) + "\n");
                    break;
                case 5:
                    bw.write((stack.isEmpty() ? -1 : stack.peek()) + "\n");
                    break;
            }
        }

        bw.flush();
        bw.close();
        br.close();
    }
}