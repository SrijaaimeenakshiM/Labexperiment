# Exp 7: Generate Three Address Code (FLEX + BISON)

**AIM:** To write a program using FLEX and BISON to generate three-address code
(TAC) for a simple arithmetic expression.

**Files:**
- `tac.l` — FLEX source
- `tac.y` — BISON grammar
- `output.txt` — compilation commands and program output

**How to run:**
```
flex tac.l
bison -d tac.y
gcc tac.tab.c lex.yy.c -o tac -lfl
./tac
```

**RESULT:** Thus, the program to generate three-address code using FLEX and BISON
was executed and verified successfully.
