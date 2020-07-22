opening_braces = '([{<'
closing_braces = ')]}>'


def is_balanced(text):
        """
        >>> stack_trace = CustomStack('(())')
        >>> stack_trace.is_balanced()
        True

        >>> stack_trace = CustomStack('((((')
        >>> stack_trace.is_balanced()
        False

        #why is this test failing?
        >>> stack_trace = CustomStack('')
        >>> stack_trace.is_balanced()
        True

        #why is this test failing?
        >>> stack_trace = CustomStack('Sensei says yes!')
        >>> stack_trace.is_balanced()
        True

        >>> stack_trace = CustomStack('))((')
        >>> stack_trace.is_balanced()
        False

        #why is this test failing?
        >>> stack_trace = CustomStack('(Sensei says yes!)')
        >>> stack_trace.is_balanced()
        True

        >>> stack_trace = CustomStack('(Sensei says no!')
        >>> stack_trace.is_balanced()
        False

        >>> stack_trace = CustomStack('(Sensei) (says) (yes!)')
        >>> stack_trace.is_balanced()
        True

        #why is this test failing?
        >>> stack_trace = CustomStack('(Sensei (says) yes!)')
        >>> stack_trace.is_balanced()
        True

        >>> stack_trace = CustomStack('((Sensei) says) no!)')
        >>> stack_trace.is_balanced()
        False

        #why is this test failing?
        >>> stack_trace = CustomStack('(Sensei (says) (yes!))')
        >>> stack_trace.is_balanced()
        True

        """
        stack = CustomStack()

        for char in text:
            if char in opening_braces:
                stack.put(char)
            elif char in closing_braces:
                if len(stack) == 0:
                    return False
                    # TODO: if opening brace does not match to the brace on top of the stack
                stack.pop()

        return not bool(stack)

class CustomStack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)

    def put(self, newItem):
        self.stack.append(newItem)

    def pop(self):
        self.stack.pop()

    def getLast(self):
        return self.stack[- 1]

    def __bool__(self):
        return bool(self.stack)



stack_trace_fail_15 = CustomStack('')
print(stack_trace_fail_15.is_balanced())  # True

stack_trace_fail_19 = CustomStack('Sensei says yes!')  # True
print(stack_trace_fail_19.is_balanced())

stack_trace_fail_27 = CustomStack('(Sensei says yes!)')  # True
print(stack_trace_fail_27.is_balanced())

stack_trace_fail_35 = CustomStack('(Sensei) (says) (yes!)')  # True
print(stack_trace_fail_35.is_balanced())

stack_trace_fail_39 = CustomStack('(Sensei (says) yes!)')  # True
print(stack_trace_fail_39.is_balanced())

stack_trace_fail_47 = CustomStack('(Sensei (says) (yes!))')  # True
print(stack_trace_fail_47.is_balanced())

if __name__ == "__main__":
    import doctest
    doctest.testmod()
