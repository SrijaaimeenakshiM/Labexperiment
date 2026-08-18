# Compiler Design Lab

A collection of **Compiler Design Laboratory experiments** implemented using **Lex/Flex and Yacc/Bison**, covering the major phases and concepts involved in compiler construction.

## 📚 About

This repository contains the programs and experiments completed as part of the **Compiler Design Laboratory**.

The experiments cover topics such as:

* Lexical Analysis
* Symbol Table Construction
* Lexical Analyzer
* Syntax Validation
* Expression Validation
* Control Structure Validation
* Calculator using Lex and Yacc
* Three Address Code Generation
* Type Checking
* Code Optimization
* 8086 Code Generation

---

## 🗂️ Repository Structure

```text
CD_LAB-main/
│
├── Exp01_Lexical_Analyzer_SymbolTable/
│   ├── README.md
│   ├── input.c
│   ├── output.txt
│   └── symtab.l
│
├── Exp02_Lexical_Analyzer/
│   ├── README.md
│   ├── iplex.c
│   ├── lexer.l
│   └── output.txt
│
├── Exp03_Arithmetic_Expression_Validation/
│   ├── README.md
│   ├── art_expr.l
│   ├── art_expr.y
│   └── output.txt
│
├── Exp04_Valid_Variable_Recognition/
│   ├── README.md
│   ├── valvar.l
│   ├── valvar.y
│   └── output.txt
│
├── Exp05_Control_Structure_Validation/
│   ├── README.md
│   ├── control.l
│   ├── control.y
│   └── output.txt
│
├── Exp06_Calculator/
│   ├── README.md
│   ├── cal.l
│   ├── cal.y
│   └── output.txt
│
├── Exp07_Three_Address_Code_Generation/
│   ├── README.md
│   ├── tac.l
│   ├── tac.y
│   └── output.txt
│
├── Exp08_Type_Checking/
│   ├── README.md
│   ├── typecheck.l
│   ├── typecheck.y
│   └── output.txt
│
├── Exp09_Code_Optimization/
│   ├── README.md
│   ├── optimize.l
│   ├── optimize.y
│   ├── sample_input.txt
│   └── output.txt
│
├── Exp10_Backend_8086_Codegen/
│   ├── README.md
│   ├── backend.l
│   ├── backend.y
│   ├── sample_input.txt
│   └── output.txt
│
└── README.md
```

---

## 🧪 Experiments

| No. | Experiment                       | Description                                              |
| --- | -------------------------------- | -------------------------------------------------------- |
| 01  | Lexical Analyzer & Symbol Table  | Identifies tokens and constructs a symbol table          |
| 02  | Lexical Analyzer                 | Performs lexical analysis of source code                 |
| 03  | Arithmetic Expression Validation | Validates arithmetic expressions using Lex and Yacc      |
| 04  | Valid Variable Recognition       | Recognizes and validates variable names                  |
| 05  | Control Structure Validation     | Validates control structures using grammar rules         |
| 06  | Calculator                       | Implements an arithmetic calculator using Lex and Yacc   |
| 07  | Three Address Code Generation    | Generates intermediate code in three-address form        |
| 08  | Type Checking                    | Performs type checking using lexical and syntax analysis |
| 09  | Code Optimization                | Demonstrates basic compiler code optimization techniques |
| 10  | 8086 Code Generation             | Generates target code for the 8086 architecture          |

---

## 🛠️ Technologies Used

* **Lex / Flex** – Lexical analysis
* **Yacc / Bison** – Syntax analysis and grammar processing
* **C** – Implementation language
* **Compiler Design Concepts**
* **8086 Assembly** – Target code generation

---

## ⚙️ Requirements

To run the experiments, install:

* GCC
* Flex
* Bison
* A terminal/command prompt

### Linux

```bash
sudo apt update
sudo apt install gcc flex bison
```

### Windows

You can use environments such as:

* WSL
* MinGW
* MSYS2

with GCC, Flex, and Bison installed.

---

## ▶️ Running Lex Programs

For a Lex program such as:

```text
lexer.l
```

compile it using:

```bash
flex lexer.l
gcc lex.yy.c -o lexer
```

Run:

```bash
./lexer
```

---

## ▶️ Running Lex + Yacc/Bison Programs

For programs containing both `.l` and `.y` files:

```bash
bison -d program.y
flex program.l
gcc lex.yy.c program.tab.c -o program
```

Run:

```bash
./program
```

For example:

```bash
bison -d cal.y
flex cal.l
gcc lex.yy.c cal.tab.c -o cal
./cal
```

---

## 📖 Concepts Covered

This laboratory repository provides practical exposure to different stages of compiler construction:

### 1. Lexical Analysis

Converts source code into a sequence of tokens such as:

* Keywords
* Identifiers
* Operators
* Constants
* Special symbols

### 2. Syntax Analysis

Uses grammar rules to determine whether a sequence of tokens follows the syntax of a language.

### 3. Intermediate Code Generation

Generates intermediate representations such as **Three Address Code (TAC)**.

Example:

```text
a = b + c * d
```

can be represented as:

```text
t1 = c * d
t2 = b + t1
a = t2
```

### 4. Type Checking

Checks whether operations are performed between compatible data types.

### 5. Code Optimization

Improves intermediate code by eliminating unnecessary computations and simplifying expressions.

### 6. Code Generation

Converts intermediate representation into target machine/assembly code, including **8086 code generation**.

---

## 📁 Experiment-wise Documentation

Each experiment contains its own `README.md` with details about the respective program, implementation, and output.

Navigate to an experiment folder to view its documentation and source code.

---

## 🎯 Learning Objectives

Through these experiments, the following skills are developed:

* Understanding lexical analysis
* Designing and implementing grammars
* Using Lex/Flex
* Using Yacc/Bison
* Constructing symbol tables
* Validating programming language constructs
* Generating intermediate code
* Performing type checking
* Applying code optimization techniques
* Understanding target code generation

---

## 👩‍💻 Author

**Dhivashini**

Computer Science and Engineering
Compiler Design Laboratory

---

## ⭐ Repository

This repository contains the complete set of Compiler Design Laboratory experiments and their corresponding source code, documentation, and sample outputs.
