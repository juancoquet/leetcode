// https://leetcode.com/problems/palindrome-number/description/


public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0 || (x % 10 == 0 && x != 0)) { 
            return false;
        }
        int rev = 0;
        while (x > rev) {
            int last = x % 10;
            rev = rev * 10 + last;
            x /= 10;
        }
        return x == rev || x == rev / 10;
    }
}
