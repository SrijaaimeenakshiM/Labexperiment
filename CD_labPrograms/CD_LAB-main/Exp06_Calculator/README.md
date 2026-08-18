# Exp 6: Calculator using LEX and YACC (BISON)

**AIM:** To write a program to implement a Calculator using FLEX and BISON.

**Files:**
- `cal.l` — FLEX source
- `cal.y` — BISON grammar
- `output.txt` — compilation commands and program output

**How to run:**
```
flex cal.l
bison -d cal.y
gcc lex.yy.c cal.tab.c -o calc -lfl
./calc
```

**RESULT:** Thus the program for implementing a calculator using FLEX and BISON was
executed and verified successfully.
