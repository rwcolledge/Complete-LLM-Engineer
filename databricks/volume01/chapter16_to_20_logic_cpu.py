# Databricks notebook source
# Volume I, Chapters 16-20: Boolean logic, adders, and a tiny CPU.

# COMMAND ----------

def half_adder(a, b):
    total = a + b
    return total % 2, total // 2

for a in (0, 1):
    for b in (0, 1):
        print(a, b, half_adder(a, b))

# COMMAND ----------

def full_adder(a, b, carry_in):
    total = a + b + carry_in
    return total % 2, total // 2

print(full_adder(1, 1, 1))

# COMMAND ----------

program = [("LOAD", 5), ("ADD", 7), ("PRINT", None)]
accumulator = 0
for instruction, value in program:
    if instruction == "LOAD":
        accumulator = value
    elif instruction == "ADD":
        accumulator += value
    elif instruction == "PRINT":
        print(accumulator)
