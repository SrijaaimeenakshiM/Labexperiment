# Exp 10: Compiler Back-End — TAC to 8086 Assembly (FLEX + BISON)

**AIM:** To write a program using FLEX and BISON to implement the back-end of a
compiler which takes three-address code (TAC) as input and generates
equivalent 8086 assembly language code.

**Files:**
- `backend.l` — FLEX source
- `backend.y` — BISON grammar
- `sample_input.txt` — sample TAC statements
- `output.txt` — compilation commands and program output

**How to run:**
```
flex backend.l
bison -d backend.y
gcc lex.yy.c backend.tab.c -o backend -lfl
./backend
```

**RESULT:** Thus, the back-end of the compiler was successfully implemented using
FLEX and BISON to translate three-address code into equivalent 8086
assembly language code.
