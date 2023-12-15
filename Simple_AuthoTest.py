from Functions import salary, hello_who

assert hello_who("Max") == "Hello, Max", "Hello who Error"
assert hello_who("Leo") == "Hello, Leo", "Hello who Error"
assert salary(2,1) == 4, "Salary Failed"
assert salary(2,2) == 8, "Salary Failed"

