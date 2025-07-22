import java.io.*;
import java.util.*;
/**
 * 2부터 올라가면서 해당 숫자를 1로 만들때 가장 적은 횟수를 쌓아서 올라감
 * arr[i]의 초기값으로 무조건 -1을 한 값을 넣어놓고 시작한 후 바로 2,3 중 하나를 나누는 것과 1을 뺀 경우 중에
 * 더 적은 횟수를 저장한다.
 * 
 * ex) n이 5의 경우
 * arr[5]에 arr[4]에 +1을 한 값을 저장한다
 * => 5에서 -1을 한 것과 동일한 효과.
 * arr[4]에는 4를 1로 만들때 최소 횟수가 저장되어 있음
 * 
 * 이렇게 2에서 부터 쌓아 올라간다.
 */

class Main{
    public static void main(String[] args) throws IOException {
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

                int n = Integer.parseInt(br.readLine());
                
                int[] arr = new int[n+1];

                for (int i=2;i<=n;i++){
                    arr[i] = arr[i-1]+1; // 현재 arr[i]에는 -1을 한 값을 저장
                    
                    if (i % 3 == 0){ 
                        arr[i] = Math.min(arr[i],arr[i/3]+1); // 바로 3을 나누는것과 -1을 한 값중에 더 작은 값
                    } 

                    if (i % 2 == 0){
                        arr[i] = Math.min(arr[i],arr[i/2]+1);// 바로 2를 나누는것과 -1을 한 값중에 더 작은 값
                    }

                }

                System.out.println(arr[n]);
    }
}