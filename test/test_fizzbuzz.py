from fizzbuzz.fizzbuzz import fizzbuzz


def test_fizzbuzz_3():
    result = fizzbuzz(3)
    assert result == ["1", "2", "Fizz"]


def test_fizzbuzz_5():
    result = fizzbuzz(5)
    assert result == ["1", "2", "Fizz", "4", "Buzz"]


def test_fizzbuzz_15():
    result = fizzbuzz(15)
    assert result == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]
