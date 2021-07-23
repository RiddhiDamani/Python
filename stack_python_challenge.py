class Stack:

    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if(self.items):
            return self.items.pop()
        else:
            return None

    def peek(self):
        if(self.items):
            return self.items[-1]
        else:
            return None

    def isempty(self):
        return self.items == []

def match_symbols(symbol_str):

    # dictionary
    symbol_pairs = {
        '(':')', 
        '{':'}',
        '[':']'
    }
    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbol_str):
        symbol = symbol_str[index]

        if symbol in openers:
            my_stack.push(symbol)
        else: # the symbol is a closer
            #if the stack is already empty, the symbols are not balanced
            if my_stack.isempty():
                return False

            # if there are still items in stack, check for a mismatch.
            else: 
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False
        index +=1

    if my_stack.isempty():
        return True

    return False #Stack iis not empty so symbols were not balanced

print(match_symbols('([{}])'))
print(match_symbols('(({}])'))
