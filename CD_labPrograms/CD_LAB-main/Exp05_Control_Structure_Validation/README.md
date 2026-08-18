# Exp 5: Recognize Valid C Control Structures (FLEX + BISON)

**AIM:** To write a program to recognize a valid control structure syntax of C
language (such as for loop, while loop, if-else, if-else-if,
switch-case, etc.) using FLEX and BISON.

**Files:**
- `control.l` — FLEX source
- `control.y` — BISON grammar
- `output.txt` — compilation commands and program output

**How to run:**
```
flex control.l
bison -d control.y
gcc lex.yy.c control.tab.c -o control -lfl
./control
```

**RESULT:** Thus the program to recognize a valid control structure syntax of C
language (For loop, while loop, if-else, if-else-if, switch-case, etc.)
using FLEX and BISON was executed and verified successfully.
