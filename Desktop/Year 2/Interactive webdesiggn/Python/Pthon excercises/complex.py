# Simple program to work with complex numbers

# Ask user to enter two complex numbers
num1 = complex(input("Enter the first complex number (e.g., 2+3j): "))
num2 = complex(input("Enter the second complex number (e.g., 1+4j): "))


sum_result = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2
div_result = num1 / num2

print("\nResults:")
print("Sum =", sum_result)
print("Difference =", diff_result)
print("Product =", product_result)
print("Division =", div_result)
