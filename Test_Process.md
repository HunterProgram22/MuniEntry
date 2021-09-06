1. Write tests
2. Clean up If/else
3. Clean up strings/magic numbers
4. Clarify function names
5. Functions do one thing
6. Store useful info at class level or global variable
7. Run and clean with Flake8
8. Run and clean with Pylint
9. Run Black then Pylint
10. Run Pytest
11. Run Rope - to make changes across codebase
12. Run Wily https://towardsdatascience.com/simplify-your-python-code-automating-code-complexity-analysis-with-wily-5c1e90c9a485
  Maintainability Index
    The MI is bound between 0 and 100 in theory but not in practice (most software implementations cap it at 100). The original paper introducing the metric noted the following thresholds: if your code’s MI is below 65 it is hard to maintain; if it’s 85 or higher, your code is easy to maintain. Anything between 65 and 85 is moderately maintainable (Coleman, Lowther, and Oman, 1994). The rescaled version (to between 0 and 100) used by Visual Studio² puts the thresholds at 0 to 9 for low maintainability, 10–19 for moderate, and 20 and above for high maintainability respectively. (Please note that different IDEs and libraries may use different thresholds.)
  Cyclomatic complexity
    The higher the value of the CYC, the more complex your code. The Software Engineering Institute at Carnegie Mellon defines the following ranges (see this publication, p. 147):
    1–10: low risk, simple program;
    11–20: moderate risk, more difficult program;
    21–50: high risk, very difficult program;
    50+: very high risk, untestable program.
13. Run pdoc
