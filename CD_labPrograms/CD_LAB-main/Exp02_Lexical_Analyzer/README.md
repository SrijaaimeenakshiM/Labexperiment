# Exp 2: Lexical Analyzer using LEX

**AIM:** To create a program that reads a C source code file and
identifies individual tokens such as identifiers, keywords, constants,
operators, preprocessor directives, header files and delimiters, using
FLEX and its built-in regular expression matching.

**Files:**
- `lexer.l` — FLEX source
- `iplex.c` — sample input C file
- `output.txt` — compilation commands and program output

**How to run:**
```
flex lexer.l
gcc lex.yy.c -o lexer -lfl
./lexer iplex.c
```

**RESULT:** Thus, the FLEX program for implementation of a Lexical Analyzer was
executed and verified successfully.
