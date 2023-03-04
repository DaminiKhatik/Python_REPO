import dis
def fib(n):   
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)

dis.dis(fib)
"""" output as......................
    2           0 RESUME                   0

  3           2 LOAD_FAST                0 (n)
              4 LOAD_CONST               1 (2)
              6 COMPARE_OP               1 (<=)        
             12 POP_JUMP_FORWARD_IF_FALSE     2 (to 18)
             14 LOAD_CONST               2 (1)
             16 RETURN_VALUE

  4     >>   18 LOAD_GLOBAL              1 (NULL + fib)
             30 LOAD_FAST                0 (n)
             32 LOAD_CONST               2 (1)
             34 BINARY_OP               10 (-)
             38 PRECALL                  1
             42 CALL                     1
             52 LOAD_GLOBAL              1 (NULL + fib)
             64 LOAD_FAST                0 (n)
             66 LOAD_CONST               1 (2)
             68 BINARY_OP               10 (-)
             72 PRECALL                  1
             76 CALL                     1
             86 BINARY_OP                0 (+)
             90 RETURN_VALUE"""