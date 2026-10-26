class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[2];
        int even = 0;
        int odd = 0;
        for (int i : num_list){
            if (i % 2 == 1){
                odd += 1;
            }
            else{
                even += 1;
            }
        }
        answer[0] = even;
        answer[1] = odd;
        return answer;
    }
}