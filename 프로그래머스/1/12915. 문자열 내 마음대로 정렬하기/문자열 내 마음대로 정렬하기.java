import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, Comparator
                    .comparingInt((String s) -> s.charAt(n))
                    .thenComparing(Comparator.naturalOrder())
                    );
        return strings;
    }
}