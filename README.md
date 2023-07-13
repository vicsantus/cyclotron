# Algorithm Cyclotron! 😊

## 🤔 Contextualizing

Low complexity algorithm (O(n)) where the cyclotron function takes two inputs. An entry is a particle, and this particle can only be "p", "n" or "e". The other entry is a matrix, where this matrix must be quadratic, that is, all lists within the matrix must have the same size as the matrix, and the matrix must also have a minimum size of 4 elements. In case something comes up outside this scope, an error should be created.

## 💎 How the project works

When using the cyclotron function with particle "n", the function returns the same matrix, however, with the list of index 0 filled by "n" until the end.

When using the cyclotron function with particle "e", the function returns the same matrix, however, with the list of index 0 filled by "e" until the end, and all the last elements of the internal lists are also transformed into "e" .

The cyclotron function with particle "p" is a little more complex, the function returns the same matrix, however, with the list of index 0 filled by "p" until the end, all the last elements of the internal lists are also transformed into " p", with the exception of the last list, because in the last list, all elements are transformed into "p", except the last element. Furthermore, in the penultimate list of the matrix, the last 2 elements are transformed into "p".

In addition to cyclotron, a file called main.py was also made. With it you can run the cyclotron function in the shell with the command `python3 main.py` inside the ./src route.


## 🛠️ Installation

Project installation

- Download the repository
```bash
  git clone git@github.com:vicsantus/cyclotron.git && cd cyclotron
```
- Install tests (Only if you want to test the project)
```bash
  python3 -m pip install -r dev-requirements.txt
```
- Test the project (Only if you want to test the project)
```bash
  python3 -m pytest -s -vv
```
- Use the main.py function (Only if you want to use the cyclotron function from the shell)
```bash
  cd src && python3 main.py
```
## Technologies

The entire project was done in **python**, and the tests were done in **pytest**.

- To install python follow the official link: https://www.python.org/downloads/

#
Code for love, love for code ♥️.