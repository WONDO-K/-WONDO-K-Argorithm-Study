import java.util.*;
import java.io.*;
import java.math.*;

class Solution {
    static Queue<int[]> que = new ArrayDeque<>();
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        que.offer(new int[]{0,0});
        while (!que.isEmpty()) {
            int[] temp = que.poll();
            int sum = temp[0];
            int idx = temp[1];

            if (idx == numbers.length){
                if(sum == target){
                    answer++;
                }
                continue;
            }
            que.offer(new int[] { sum + numbers[idx], idx + 1 });
            que.offer(new int[] { sum - numbers[idx], idx + 1 });

            }

            return answer; 
        }
}