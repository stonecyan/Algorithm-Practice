def fizzBuzz(self, n):
    array = []
    i = 1
    while i <= n:
        if i % 15 == 0:
            array.append("FizzBuzz")
        elif i % 3 == 0:
            array.append("Fizz")
        elif i % 5 == 0:
            array.append("Buzz")
        else:
            array.append(str(i))
        i += 1
    return array
