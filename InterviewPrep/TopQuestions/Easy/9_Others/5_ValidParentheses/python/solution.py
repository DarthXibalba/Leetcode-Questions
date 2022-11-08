from collections import deque

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    openers = "({["
    closers = ")}]"
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }
    stack = deque()
    for c in s:
        if c in openers:
            stack.append(c)
        # c must be a closer, so pop the stack to reveal if it is a match or not
        else:
            # EDGE CASE: If there have been no openers added to stack, then we do not have a valid parenthesis
            if len(stack) == 0:
                return False
            # If the opener does not match the pair of c
            if stack.pop() != pairs[c]:
                return False
    # EDGE CASE: If there are still openers in the stack, then there was no matching closer found
    if len(stack) == 0:
        return True
    else:
        return False



if __name__ == '__main__':
    inputs = [
        "()",
        "()[]{}",
        "(]",
        "[",
        "]"
    ]
    answers = [
        True,
        True,
        False,
        False,
        False
    ]
    for i in range(len(inputs)):
        ans = isValid(inputs[i])
        print(inputs[i])
        print(ans)
        assert answers[i] == ans, f"{answers[i]} != {ans}"
        print()
