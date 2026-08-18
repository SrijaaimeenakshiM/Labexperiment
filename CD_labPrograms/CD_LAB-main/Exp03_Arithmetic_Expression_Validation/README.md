# Exp 3: Recognize a Valid Arithmetic Expression (FLEX + BISON)

**AIM:** To write a program to recognize a valid arithmetic expression that uses
operator +, -, * and / using FLEX and BISON.

**Files:**
- `art_expr.l` — FLEX source
- `art_expr.y` — BISON grammar
- `output.txt` — compilation commands and program output

**How to run:**
```
flex art_expr.l
bison -d art_expr.y
gcc lex.yy.c art_expr.tab.c -o art_expr -lfl
./art_expr
```

**RESULT:** Thus the program to recognize a valid arithmetic expression that uses
operator +, -, * and / using FLEX and BISON was executed and verified
successfully.
