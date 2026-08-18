# Exp 8: Type Checking (FLEX + BISON)

**AIM:** To write a program using FLEX and BISON to implement type checking of
variables in simple declarations and expressions, using a symbol table
built during parsing.

**Files:**
- `typecheck.l` — FLEX source
- `typecheck.y` — BISON grammar
- `output.txt` — compilation commands and program output

**How to run:**
```
flex typecheck.l
bison -d typecheck.y
gcc lex.yy.c typecheck.tab.c -o typecheck -lfl
./typecheck
```

**RESULT:** Thus, the FLEX and BISON program for type checking was successfully
implemented. The program builds a symbol table from declarations and
checks type consistency in assignment expressions.
