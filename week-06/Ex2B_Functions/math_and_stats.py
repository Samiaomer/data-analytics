# --- Imports ---
import random
import math
import statistics

# --- Starting Variables ---

# A range of values from 1 to 99
vals_1_100 = range(1, 100)

# 75 unique random values pulled from vals_1_100 (no repeats)
vals_sample = random.sample(vals_1_100, 75)

# 200 random values pulled from vals_1_100 (repeats allowed)
vals_choices = random.choices(vals_1_100, k=200)

# A random integer between 3 and 10 (inclusive) for the radius
radius = random.randint(3, 10)

# Pi constant from the math module
pi = math.pi

# --- Quick check: print everything to verify ---
print("vals_sample:", vals_sample)
print("vals_choices:", vals_choices)
print("radius:", radius)
print("pi:", pi)

# ============================================================
# Exercise 2B - Math and Stats
# ============================================================

# --- Imports ---
import random
import math
import statistics

# --- Starting Variables ---
vals_1_100 = range(1, 100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)
radius = random.randint(3, 10)
pi = math.pi

# ============================================================
# SECTION 1: Subset calculations (75 sample values)
# ============================================================

# Sum of all 75 sample values
sample_sum = sum(vals_sample)

# Average (mean) of the 75 sample values
sample_avg = statistics.mean(vals_sample)

# Median (middle value) of the 75 sample values
sample_median = statistics.median(vals_sample)

# ============================================================
# SECTION 2: Superset calculations (200 values)
# ============================================================

# Average (mean) of the 200 values
choices_avg = statistics.mean(vals_choices)

# Median of the 200 values
choices_median = statistics.median(vals_choices)

# Mode (most frequently occurring value) of the 200 values
choices_mode = statistics.mode(vals_choices)

# Standard deviation of the 200 values
choices_stdev = statistics.stdev(vals_choices)

# Variance of the 200 values
choices_variance = statistics.variance(vals_choices)

# ============================================================
# SECTION 3: Circle calculations
# formula: area = pi * radius squared
# ============================================================

# Calculate raw area of circle
circle_area = pi * (radius ** 2)

# Rounded UP to nearest integer using math.ceil()
area_rounded_up = math.ceil(circle_area)

# Rounded DOWN to nearest integer using math.floor()
area_rounded_down = math.floor(circle_area)

# ============================================================
# PRINT OUTPUT
# ============================================================

print("_Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:", sample_sum)
print("Average of 75 sample values:", sample_avg)
print("Median of 75 sample values:", sample_median)

print('\n')

print("_Experimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", choices_avg)
print("Median of 200 values:", choices_median)
print("Mode of 200 values:", choices_mode)
print("Standard deviation of 200 values:", choices_stdev)
print("Variance of 200 values:", choices_variance)

print('\n')

print("_Modeling a random circle:")
print("Radius =", radius, ", area =", area_rounded_up, "(rounded up to the nearest integer)")
print("Radius =", radius, ", area =", area_rounded_down, "(rounded down to the nearest integer)")