import math
# Basic mathematical operations
print(math.sqrt(25))       # Square root → 5.0
print(math.pow(2, 3))      # Power → 2³ = 8.0
print(math.ceil(4.2))      # Ceiling → 5
print(math.floor(4.8))     # Floor → 4
print(math.trunc(4.9))     # Truncate → 4
print(abs(-10))            # Absolute value → 10

#Trigonometric functions

print(math.sin(math.pi / 2))  # sin(90°) = 1.0
print(math.cos(0))            # cos(0°) = 1.0
print(math.tan(math.pi / 4))  # tan(45°) = 1.0

# Convert between radians and degrees
print(math.degrees(math.pi))   # 180.0
print(math.radians(180))       # 3.141592653589793
# Logarithmic and exponential functions
print(math.log(10))        # Natural log (base e)
print(math.log10(100))     # Log base 10 → 2.0
print(math.exp(2))         # e^2 → 7.389...
#Constants
print(math.pi)   # 3.141592653589793
print(math.e)    # 2.718281828459045
print(math.tau)  # 6.283185307179586 (2π)

#Other useful functions

print(math.factorial(5))   # 5! = 120
print(math.gcd(12, 18))    # GCD = 6
print(math.fabs(-7.5))     # 7.5 (float abs)
print(math.isfinite(100))  # True
print(math.isinf(float('inf'))) # True
print(math.isnan(float('nan'))) # True



