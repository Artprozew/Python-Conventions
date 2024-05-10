"""
This script tries to explain the most common conventions used, according to PEP8.
May have excessive comments to explain better the used conventions or how the code is running.
"""

from math_module.module1 import (
    MathClass,
)  # src/python_conventions/math_module/module1.py
# It's better to go check it out before anything else


def main():
    math_class = MathClass("Hello MathClass World")
    print("Message:", math_class.get_message())  # Outputs Hello MathClass World
    print("Add:", math_class.add(6, 4))
    print(
        f"Subtract method: {math_class.subtract(1, 2)}, Results variable: {math_class.sum_results}"
    )
    print("PI Constant:", math_class.get_pi(), math_class.PI_CONSTANT)  # Both will work
    # print(math_class.__private_variable)
    """ We "can't" access the private variable from outside of the Class;
    AttributeError: 'MathClass' object has no attribute '__private_variable' """
    print(
        "Private variable:", math_class.get_private_variable()
    )  # The only way to access the private variable


if __name__ == "__main__":  # Necessary as the "main" script
    main()
