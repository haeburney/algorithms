import java.util.Arrays;

class Solution {
    public int[] solution(String s) {
        
        int[] answer = new int[s.length()];
		int[] isDuplication = new int[26];
		Arrays.fill(isDuplication, -1);
		
		for (int i = 0; i < s.length(); i++) {
			int index = (int) s.charAt(i) - 97;

			if (isDuplication[index] == -1) {
				answer[i] = -1;
			} else {
				answer[i] = i - isDuplication[index];
			}
			isDuplication[index] = i;
		}
        
        return answer;
    }
}