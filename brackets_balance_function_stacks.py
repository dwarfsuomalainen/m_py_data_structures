'''You have to write a function named "check_balance" that checks whether a string with different kind of bracket symbols is balanced or not using stack. The stack class is already available with the name "Stack"

The function "check_balance" accepts a string and it will check if the different sets of brackets symbols in the text are balanced, i.e. every kind of open bracket symbol is closed with the same kind of bracket symbol ('()', '[]' or '{}'). If everything checks, the function should return the text "Ok - C", being C the number of pairs found. If not, it should return the text: "Match error at position X", being X the position of the character relative to the beginning of the text.

Notice that texts should be exactly like shown and with the same capitalization.

The idea is simple, when you encounter an opening bracket symbol (`(` or a `{` or a `[`) you will push it to the stack. When you encounter a closing bracket symbol (`)` or a `}` or a `]`), pop the one in the stack and check if they match. If they don't match, you can return the error. If you get to the end of text without errors, return the "Ok" text as told before.


Some cases you want to take into account are when you encounter a closing bracket symbol before any opening one, and when the text leaves an unmatched opening bracket symbol.

Esimerkiksi:

Syöte	Tulos
a(b)c[d]e{f}g
Ok - 3
'''
from data_structs_stacks_push_pop_methods import Stack

def check_balance(text):
    #print(text)
    pairs = 0
    stack_sym = Stack()
    position = 0
    if not text:
        print("Ok - 0")
        return
    for symb in text:
        '''if symb in (')', ']', '}') and position == 0:
            print ("Match error at position 0")
            return'''
        if symb in ('(','[','{'):
            #print(symb)
            to_push = (symb, position)
            stack_sym.push(to_push)
            #print(stack_sym)
        if symb in (')', ']', '}'):
            #print(symb)
            pairs += 1
            val = stack_sym.pop()
            if not val:
                print(f'Match error at position {position}')
                return
            if val[0] == '(' and symb != ')':
                print(val)
                #print(f"Match error at position {val[1]}")
                print(f"Match error at position {position}")
                return

            if val[0] == '[' and symb != ']':
                print(val)
                #print(f"Match error at position {val[1]}")
                print(f"Match error at position {position}")
                return

            if val[0] == '{' and symb != '}':
                print(val)
                #print(f"Match error at position {val[1]}")
                print(f"Match error at position {position}")
                return
        position += 1
    if stack_sym.__len__() != 0:
        print(f"Match error at position {position - 1}")
        return
    else:
        print (f"Ok - {pairs}")
        return


def main():
    #check_balance("a(b)c[d]e{f}g")
    #check_balance("a(b)c[)d]e{f}g")
    #check_balance("a(b)(((c[d]e{f}g)))")
    #check_balance("a(b)c(([d][e{f}])g)")
    check_balance("a(b)c(([d][e{f}]))g)((")
    #check_balance("]a(b)c(([d][e{f}])g)")
    #check_balance(abc)
main()