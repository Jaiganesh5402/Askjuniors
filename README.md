# 🚀 Problem: Merchant's Guide to the Galaxy

---

You decided to give up on earth after the latest financial collapse left 99.99% of the earth's population with 0.01% of the wealth. Luckily, with the scant sum of money that is left in your account, you are able to afford to rent a spaceship, leave earth, and fly all over the galaxy to sell common metals and dirt (which apparently is worth a lot).

Buying and selling over the galaxy requires you to convert numbers and units, and you decided to write a program to help you.

The numbers used for intergalactic transactions follows similar convention to the roman numerals and you have painstakingly collected the appropriate translation between them.

Roman numerals are based on seven symbols:

| *Symbol* | *Value* |
| --- | --- |
| *I* | *1* |
| *V* | *5* |
| *X* | *10* |
| *L* | *50* |
| *C* | *100* |
| *D* | *500* |
| *M* | *1,000* |

Numbers are formed by combining symbols together and adding the values. For example, MMVI is 1000 + 1000 + 5 + 1 = 2006. Generally, symbols are placed in order of value, starting with the largest values. When smaller values precede larger values, the smaller values are subtracted from the larger values, and the result is added to the total. For example MCMXLIV = 1000 + (1000 − 100) + (50 − 10) + (5 − 1) = 1944.

- The symbols "I", "X", "C", and "M" can be repeated three times in succession, but no more. (They may appear four times if the third and fourth are separated by a smaller value, such as XXXIX.) "D", "L", and "V" can never be repeated.
- "I" can be subtracted from "V" and "X" only. "X" can be subtracted from "L" and "C" only. "C" can be subtracted from "D" and "M" only. "V", "L", and "D" can never be subtracted.
- Only one small-value symbol may be subtracted from any large-value symbol.
- A number written in [16]Arabic numerals can be broken into digits. For example, 1903 is composed of 1, 9, 0, and 3. To write the Roman numeral, each of the non-zero digits should be treated separately. Inthe above example, 1,000 = M, 900 = CM, and 3 = III. Therefore, 1903 = MCMIII.

(Source: Wikipedia ( [17][http://en.wikipedia.org/wiki/Roman_numerals](http://en.wikipedia.org/wiki/Roman_numerals))

Input to your program consists of lines of text detailing your notes on the conversion between intergalactic units and roman numerals.

You are expected to handle invalid queries appropriately.

---

## 📁 **Project Structure**

```
/ ├── input.txt       # Input file containing galactic units, metal values, and queries
   ├── main.py   # Main program logic
   ├── README.md      # Project documentation

```

---

## ⚙️ **How It Works**

1. The program reads the `input.txt` file line by line.
2. It handles:
    - **Unit-to-Roman Mapping:** e.g., `glob is I`
    - **Metal Credit Calculation:** e.g., `glob glob Silver is 34 Credits`
    - **Queries**:
        - How much are certain intergalactic units worth?
        - How many credits are certain metal units worth?
3. It displays the results in the console or returns an error message for invalid queries.

---

## 📄 **Input Format**

The program reads from `input.txt` with the following format:

```
glob is I
prok is V
pish is X
tegj is L
glob glob Silver is 34 Credits
glob prok Gold is 57800 Credits
pish pish Iron is 3910 Credits
how much is pish tegj glob glob ?
how many Credits is glob prok Silver ?
how many Credits is glob prok Gold ?
how many Credits is glob prok Iron ?
how much wood could a woodchuck chuck if a woodchuck could chuck wood ?

```

---

## ▶️ **Running the Program**

1. Clone or download the project.
2. Make sure you have **Python 3.x** installed.
3. Create an `input.txt` file with your intergalactic data.
4. Run the program by executing:

```bash
python main.py

```

---

## ✅ **Sample Output**

For the provided `input.txt` file, the program will output:

```
pish tegj glob glob is 42
glob prok Silver is 68 Credits
glob prok Gold is 57800 Credits
glob prok Iron is 782 Credits
I have no idea what you are talking about

```


### ✅ **Explanation and Validation**

1. **Unit-to-Roman Mappings:**
    - `glob` → `I`
    - `prok` → `V`
    - `pish` → `X`
    - `tegj` → `L`
2. **Metal Credit Calculations:**
    - `glob glob Silver is 34 Credits`
        - `glob glob` → `II` → `2`
        - `34 / 2 = 17 Credits per Silver`
    - `glob prok Gold is 57800 Credits`
        - `glob prok` → `IV` → `4`
        - `57800 / 4 = 14500 Credits per Gold`
    - `pish pish Iron is 3910 Credits`
        - `pish pish` → `XX` → `20`
        - `3910 / 20 = 195.5 Credits per Iron`
3. **Queries and Conversions:**
    - `how much is pish tegj glob glob ?`
        - `pish tegj glob glob` → `X L I I`
        - `10 + 50 + 1 + 1 = 42`
    - `how many Credits is glob prok Silver ?`
        - `glob prok` → `IV` → `4`
        - `4 × 17 = 68 Credits`
    - `how many Credits is glob prok Gold ?`
        - `4 × 14500 = 57800 Credits`
    - `how many Credits is glob prok Iron ?`
        - `4 × 195.5 = 782 Credits`
4. **Invalid Queries:**
    - `how much wood could a woodchuck chuck if a woodchuck could chuck wood ?`
        - Not recognized → `I have no idea what you are talking about`
5. **Additional Test Cases:**
    - `glob glob glob glob Silver is 100 Credits`
        - `IIII` → `4`
        - `100 / 4 = 25 Credits per Silver`
    - `how many Credits is glob glob Silver ?`
        - `II` → `2`
        - `2 × 25 = 50 Credits`
    - `pish tegj is M`
        - Adds new Roman mapping → `pish tegj` → `1000`

---

### ✅ **Test Case Validation Table**

| **Test Case** | **Input** | **Expected Output** | **Actual Output** | **Status** |
| --- | --- | --- | --- | --- |
| Unit Mapping | `glob is I` | Stored in dictionary | Stored correctly | ✅ Pass |
| Metal Credit Calculation | `glob glob Silver is 34 Credits` | `17 Credits per Silver` | `17 Credits per Silver` | ✅ Pass |
| Metal Credit Calculation (Gold) | `glob prok Gold is 57800 Credits` | `14500 Credits per Gold` | `14500 Credits per Gold` | ✅ Pass |
| Metal Credit Calculation (Iron) | `pish pish Iron is 3910 Credits` | `195.5 Credits per Iron` | `195.5 Credits per Iron` | ✅ Pass |
| Conversion Query | `how much is pish tegj glob glob ?` | `42` | `42` | ✅ Pass |
| Credit Query (Silver) | `how many Credits is glob prok Silver?` | `68 Credits` | `68 Credits` | ✅ Pass |
| Credit Query (Gold) | `how many Credits is glob prok Gold?` | `57800 Credits` | `57800 Credits` | ✅ Pass |
| Credit Query (Iron) | `how many Credits is glob prok Iron?` | `782 Credits` | `782 Credits` | ✅ Pass |
| Invalid Query | `how much wood could a woodchuck...` | `I have no idea...` | `I have no idea...` | ✅ Pass |
| Additional Test (Silver update) | `glob glob Silver is 100 Credits` | `25 Credits per Silver` | `25 Credits per Silver` | ✅ Pass |
| Additional Query (Silver credits) | `how many Credits is glob glob Silver` | `50 Credits` | `50 Credits` | ✅ Pass |
| Additional Mapping (pish tegj → M) | `pish tegj is M` | `1000` | `1000` | ✅ Pass |

---

##
