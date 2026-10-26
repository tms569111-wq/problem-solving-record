class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        for (String s : my_string.split("")){
            for (int i = 0; i < n; i++){
                answer += s;
            }
        }
        return answer;
    }
}