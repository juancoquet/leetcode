// https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

public class Solution {
    public int EvalRPN(string[] tokens)
    {
        Stack stack = new Stack();

        foreach (string t in tokens)
        {
            int num;
            bool isInt = int.TryParse(t, out num);
            if (isInt)
            {
                stack.Push(num);
            }
            else
            {
                int b = (int)stack.Pop();
                int a = (int)stack.Pop();
                int res;
                switch (t)
                {
                    case "*":
                        res = a * b;
                        break;
                    case "/":
                        res = a / b;
                        break;
                    case "+":
                        res = a + b;
                        break;
                    default:  // "-"
                        res = a - b;
                        break;
                }
                stack.Push(res);
            }
        }
        return (int)stack.Pop();
    }
}
