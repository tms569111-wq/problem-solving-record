import java.util.Arrays;

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        return Arrays.stream(numbers).average().orElse(0);
    }
}