import sys
#sys.maxsize = 2**3-1
#so I don't have to write my own function to enforce bit sizes...
#will change the environment properly be rebuilding the python executable....
class Solution:
    def reverse1(self, x: int) -> int:
        # Check if the number is negative
        negative = x < 0

        # Convert the number to a string and reverse it
        x_str = str(abs(x))
        x_str_rev = x_str[::-1]

        # Convert the reversed string back to an integer
        x_rev = int(x_str_rev)
        x_rev = self.enforce_32_bit(x_rev)

        # Apply the sign to the reversed integer
        if negative:
            x_rev = -x_rev
            x_rev = self.enforce_32_bit(x_rev)

        # Check if the reversed integer is within the 32-bit range
        if x_rev < -2 ** 31 or x_rev > 2 ** 31 - 1:
            return 0

        return x_rev

    def reverse2(self, x: int) -> int:
        # Check if the number is negative
        negative = x < 0

        # Convert the number to a string and reverse it
        x_str = str(abs(x))
        x_str_rev = x_str[::-1]

        # Try to convert the reversed string back to an integer
        try:
            x_rev = int(x_str_rev)
            x_rev = self.enforce_32_bit(x_rev)
        except OverflowError:
            # Return 0 if the reversed integer is outside the 32-bit range
            return 0

        # Apply the sign to the reversed integer
        if negative:
            x_rev = -x_rev
            x_rev = self.enforce_32_bit(x_rev)

        # Check if the reversed integer is within the 32-bit range
        if x_rev < -2 ** 31 or x_rev > 2 ** 31 - 1:
            return 0

        return x_rev

    def reverse3(self, x: int) -> int:
        # Check if the number is negative
        negative = x < 0

        # Convert the number to a string and reverse it
        x_str = str(abs(x))
        x_str_rev = x_str[::-1]

        # Convert the reversed string back to an integer digit by digit
        x_rev = 0
        for digit in x_str_rev:
            x_rev = self.enforce_32_bit(x_rev*10) + int(digit)
            x_rev = self.enforce_32_bit(x_rev)

        # Apply the sign to the reversed integer
        if negative:
            x_rev = -x_rev
            x_rev = self.enforce_32_bit(x_rev)

        # Check if the reversed integer is within the 32-bit range
        if x_rev < -2 ** 31 or x_rev > 2 ** 31 - 1:
            return 0

        return x_rev

    def reverse4(self, x: int) -> int:
        # Check if the number is negative
        negative = x < 0

        # Convert the number to a string and reverse it
        x_str = str(abs(x))
        x_str_rev = x_str[::-1]

        # Convert the reversed string back to an integer digit by digit
        x_rev = 0
        for digit in x_str_rev:
            x_rev = self.enforce_32_bit(x_rev)

            quotient, remainder = divmod(self.enforce_32_bit(x_rev*10), self.enforce_32_bit(2**31))
            quotient = self.enforce_32_bit(quotient)
            remainder=self.enforce_32_bit(remainder)
            if quotient != 0:
                return 0
            x_rev = self.enforce_32_bit(quotient + remainder) + int(digit)
            x_rev = self.enforce_32_bit(x_rev)

        # Apply the sign to the reversed integer
        if negative:
            x_rev = -x_rev
            x_rev = self.enforce_32_bit(x_rev)

        return x_rev

    def reverse5(self, x: int) -> int:
        # Check if the number is negative
        negative = x < 0

        # Convert the number to a string and reverse it
        x_str = str(abs(x))
        x_str_rev = x_str[::-1]

        # Convert the reversed string back to an integer digit by digit
        x_rev = 0
        for digit in x_str_rev:
            if x_rev > self.enforce_32_bit(2**31) // 10:
                return 0

            x_rev = self.enforce_32_bit(x_rev*10) + int(digit)
            x_rev = self.enforce_32_bit(x_rev)

        # Apply the sign to the reversed integer
        if negative:
            x_rev = -x_rev
            x_rev = self.enforce_32_bit(x_rev)

        # Check if the reversed integer is within the 32-bit range
        if x_rev < -2 ** 31 or x_rev > 2 ** 31 - 1:
            return 0

        return x_rev

    def reverse6(self, x: int) -> int:
        result = 0
        while x != 0:
            digit = x % 10
            new_result = self.enforce_32_bit(result*10) + digit
            new_result = self.enforce_32_bit(new_result)
            #self.check_size(new_result)
            if self.enforce_32_bit(new_result - digit) // 10 != result:
                return 0
            result = new_result
            result = self.enforce_32_bit(result)
            x //= 10
        return result

    def enforce_32_bit(self, x):
        #if x>2*31-1
        if x > 2**31-1:
            overflow = x - (2**31-1)
            x = overflow-1 + -2**31
            return self.enforce_32_bit(x)
        elif x < -2 ** 31:
            underflow = -2**31 - x
            x = 1+(2**31-1)-underflow
            return self.enforce_32_bit(x)
        else:
            return x

    def reverse_integer_29_bit_1(self,x):
        # Define the integer limits for a signed 29-bit integer
        INT_MIN = -2 ** 28
        INT_MAX = 2 ** 28 - 1

        # Convert x to positive if it's negative, and store the sign
        sign = -1 if x < 0 else 1
        x *= sign
        x = self.enforce_29_bit(x)

        # Reverse the digits of x
        rev = 0
        while x > 0:
            rev =self.enforce_29_bit( self.enforce_29_bit( rev * 10) + x % 10)
            x //= 10
            x = self.enforce_32_bit(x)

        # Apply the sign to the reversed integer
        rev *= sign
        rev = self.enforce_29_bit(rev)

        # Check if the reversed integer is within the 29-bit integer range
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        else:
            return rev

    def reverse_integer_29_bit_2(x):
        # Define the integer limits for a signed 29-bit integer
        INT_MIN = -2 ** 28
        INT_MAX = 2 ** 28 - 1

        # Convert x to positive if it's negative, and store the sign
        sign = -1 if x < 0 else 1
        x *= sign
        x = enforce_29_bit(x)

        # Reverse the digits of x using string manipulation
        rev_str = str(x)[::-1]
        rev = enforce_29_bit(int(rev_str))

        # Apply the sign to the reversed integer
        rev *= sign
        rev = enforce_29_bit(rev)

        # Check if the reversed integer is within the 29-bit integer range
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        else:
            return rev

    def reverse_integer_29_bit_3(x):
        # Define the integer limits for a signed 29-bit integer
        INT_MIN = -2 ** 28
        INT_MAX = 2 ** 28 - 1

        # Convert x to positive if it's negative, and store the sign
        sign = -1 if x < 0 else 1
        x *= sign
        x = enforce_29_bit(x)

        # Reverse the digits of x using bit manipulation
        rev = 0
        while x > 0:
            rev = (rev << 1) | (x & 1)
            rev = enforce_29_bit(rev)
            x >>= 1
            x = enforce_29_bit(x)

        # Apply the sign to the reversed integer
        rev *= sign
        rev = enforce_29_bit(rev)
        # Check if the reversed integer is within the 29-bit integer range
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        else:
            return rev

    def enforce_29_bit(self, x):
        #if x>2*31-1
        if x > 2**28-1:
            overflow = x - (2**28-1)
            x = overflow-1 + -2**28
            return self.enforce_32_bit(x)
        elif x < -2 ** 28:
            underflow = -2**28 - x
            x = 1+(2**28-1)-underflow
            return self.enforce_32_bit(x)
        else:
            return x


s = Solution()
print("Testing 32 bit solution")
solutions_32 = [s.reverse1,s.reverse2,s.reverse3,s.reverse4,s.reverse5,s.reverse6]
test_nums_32 = [2**31-1,-2**31,-2**31+1,10,100,101,12,-10,-100,-12]
for i in range(len(solutions_32)):
    for n in test_nums_32:
        print(f'solution {i+1:d} on {n:d} : {solutions_32[i](n):d}')


print("Testing 29 bit solution")
solutions_29 = [s.reverse_integer_29_bit_1,s.reverse_integer_29_bit_2,s.reverse_integer_29_bit_3]
test_nums_29 = [2**28-1,-2**28,-2**28+1,10,100,101,12,-10,-100,-12]
for i in range(len(solutions_29)):
    for n in test_nums_29:
        print(f'solution {i+1:d} on {n:d} : {solutions_32[i](n):d}')