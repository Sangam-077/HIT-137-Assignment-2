# HIT137 — Group Assignment 2

**Course:** HIT137 — Software Now  
**Semester:** Semester 1, 2026  


---

## 👥 Group Members

| Name | Role |
|------|------|
| Aakriti B C | Student |
| Hemraj Budhathoki | Student |
| Sangam GC | Student |
| Sujan Gautam | Student |

---

## 📁 Repository Structure

```
├── Question1/
│   ├── question1.py
│   ├── raw_text.txt
│   ├── encrypted_text.txt
│   └── decrypted_text.txt
├── Question2/
│   ├── evaluator.py
│   ├── sample_input.txt
│   └── output.txt
├── github_link.txt
└── README.md
```

---

## 📝 Assignment Overview

### Question 1 — Text Encryption & Decryption
A Python program that:
- Reads a text file (`raw_text.txt`)
- Encrypts its contents using a shift-based cipher with two user-provided values (`shift1`, `shift2`)
- Decrypts the encrypted file back to its original form
- Verifies that the decryption matches the original file

### Question 2 — Mathematical Expression Evaluator
A Python program that:
- Reads mathematical expressions from a text file (one per line)
- Tokenises each expression
- Builds a parse tree using recursive descent parsing
- Evaluates each expression
- Writes results to `output.txt` in the required format

---

## ▶️ How to Run

### Question 1
```bash
cd Question1
python question1.py
```
When prompted, enter values for `shift1` and `shift2`.

### Question 2
```bash
cd Question2
python evaluator.py
```
Reads from `sample_input.txt` and writes results to `output.txt`.

---

## 🔗 GitHub Repository

See `github_link.txt` for the public repository link.
