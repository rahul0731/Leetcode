class MinStack {

    /** initialize your data structure here. */
    
    Stack<Integer> stack = new Stack();
     Stack<Integer> minStack = new Stack(); // keeps track of minimums

    // Always push onto stack. If it's a minimum, also push it onto minStack
    public void push(int x) {
        stack.push(x);
        if (minStack.isEmpty() || x <= getMin()) {
            minStack.push(x);
        }
    }

    // Pop off stack. If we popped a minimum, we remove it from minStack also
    public void pop() {
        if (stack.isEmpty()) {
            return;
        }
        int x = stack.pop();
        if (x == minStack.peek()) {
            minStack.pop();
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
