class Solution {
    public static int solution(int n, int w, int num) {
        int answer = 0;
        int row = (n + w - 1) / w;
        int[][] arr = new int[row][w];
        int start = 1;
        boolean flag = true; // true 오른쪽, flase 왼쪽
        int i = row-1;
        int j = 0;
        while (start<=n) {
            if (flag==true){
                while (j<w && start<=n) {
                    arr[i][j++] = start++;
                }
                i--; 
                j--;
                flag=false;// while문 종료 시 방향 전환
            } else{
                while (0<=j && start<=n) {
                    arr[i][j--] = start++;
                }
                i--;
                j++;
                flag=true;
            }
        }
        // 박스 찾기
        int box_i = 0;
        int box_j = 0;
        for (i=0;i<arr.length;i++){
            for (j=0;j<w;j++){
                if (arr[i][j]==num){
                    box_i = i;
                    box_j = j;
                    break;
                }
            }
        }

        for (i=box_i;i>-1;i--){
            if(arr[i][box_j]!=0){
                answer++;
            }
        }

        return answer;

    }
}