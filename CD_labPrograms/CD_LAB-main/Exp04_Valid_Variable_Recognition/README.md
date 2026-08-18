# Exp 4: Recognize a Valid Variable Name (FLEX + BISON)

**AIM:** To write a program to recognize a valid variable which starts with a
letter followed by any number of letters or digits using FLEX and BISON.

**Files:**
- `valvar.l` — FLEX source
- `valvar.y` — BISON grammar
- `output.txt` — compilation commands and program output

**How to run:**
```
flex valvar.l
bison -d valvar.y
gcc lex.yy.c valvar.tab.c -o valvar -lfl
./valvar
```

**RESULT:** Thus the program to recognize a valid variable which starts with a
letter followed by any number of letters or digits using FLEX and BISON
was executed and verified successfully.
