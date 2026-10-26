class Solution {
    public int solution(int slice, int n) {
        float answer = (float) n / (float) slice + (float) 0.9 ;
        return (int) answer;
    }
}