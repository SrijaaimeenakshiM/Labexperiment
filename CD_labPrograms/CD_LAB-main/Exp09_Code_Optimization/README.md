# Exp 9: Simple Code Optimization Techniques (FLEX + BISON)

**AIM:** To write a program using FLEX and BISON to implement simple code
optimization techniques such as constant folding, strength reduction and
algebraic simplification, applied while parsing three-address code style
assignment statements.

**Files:**
- `optimize.l` — FLEX source
- `optimize.y` — BISON grammar
- `sample_input.txt` — sample TAC statements
- `output.txt` — compilation commands and program output

**How to run:**
```
flex optimize.l
bison -d optimize.y
gcc lex.yy.c optimize.tab.c -o optimize -lfl
./optimize
```

**RESULT:** Thus, the FLEX and BISON program for simple code optimization
techniques - constant folding, strength reduction, and algebraic
simplification - was successfully implemented and tested with various
inputs.
