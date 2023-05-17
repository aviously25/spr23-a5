#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

# Checks that the program outputs "15" for an input of "5 + 10"
assert run("5 + 10").output == "15"
# Checks that the program outputs "20" for an input of "20 * 1"
assert run("20 * 1").output == "20"
# Checks that the program exists successfully (no error) for input "2 * 4"
assert run("13 * 4").exit_status == 0
# Checks that the program fails (correctly errors) for input "2 @ 3"
assert run("9 @$ 9").exit_status != 0

###

print("All tests passed!")
