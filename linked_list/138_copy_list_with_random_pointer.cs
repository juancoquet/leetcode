// https://leetcode.com/problems/copy-list-with-random-pointer/description/

/*
// Definition for a Node.
public class Node {
    public int val;
    public Node next;
    public Node random;
    
    public Node(int _val) {
        val = _val;
        next = null;
        random = null;
    }
}
*/

public class Solution {
    public Node CopyRandomList(Node head) {
        if (head == null) { return null; }

        Dictionary<Node, Node> copyMap = new Dictionary<Node, Node>();
        Node curr = head;
        while (curr != null) {
            Node copy = CopyGetNode(curr, copyMap);
            copy.next = CopyGetNode(curr.next, copyMap);
            copy.random = CopyGetNode(curr.random, copyMap);
            curr = curr.next;
        }
        return copyMap[head];
    }

    public Node CopyGetNode(Node node, Dictionary<Node, Node> dict) {
        if (node == null) { return null; }
        if (!dict.ContainsKey(node)) {
            Node copy = new Node(node.val);
            dict.Add(node, copy);
        }
        return dict[node];
    }
}
