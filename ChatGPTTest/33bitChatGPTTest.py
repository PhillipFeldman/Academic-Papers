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
            self.enforce_32_bit(result)
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


s = Solution()
#solutions 4,5,6 pass
print(s.reverse6(-2**31+0))