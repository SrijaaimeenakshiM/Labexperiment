# Exp 1: Lexical Analyzer with Symbol Table (FLEX)

**AIM:** To develop a lexical analyzer using FLEX to recognize tokens such as
identifiers, constants, comments, and operators in a C program and to
create a symbol table while recognizing identifiers.

**Files:**
- `symtab.l` — FLEX source
- `input.c` — sample input file
- `output.txt` — compilation commands and program output

**How to run:**
```
flex symtab.l
gcc lex.yy.c -o symtab -lfl
./symtab input.c
```

**RESULT:** Thus the FLEX program to develop a lexical analyzer recognizing
identifiers, constants, comments and operators, and to build a symbol
table, was executed and verified successfully.
