import pytest
from .typechecking_decorator import typecheck
from typing import Union, Iterable, Tuple
# Test function with correct types
@typecheck
def add_numbers(a: int, b: int) -> int:
    return a + b

# Test function with incorrect return type
@typecheck
def add_strings(a: str, b: str) -> int:
    return a + b

# Test function with Union type
@typecheck
def process_value(value: Union[int, str]) -> Union[int, str]:
    return value

# Test function with Iterable type
@typecheck
def sum_elements(elements: Iterable[int]) -> int:
    return sum(elements)

# Test function with Tuple type
@typecheck
def get_coordinates() -> Tuple[int, int]:
    return (10, 20)

# Test function with incorrect argument type
@typecheck
def multiply_numbers(a: int, b: str) -> int:
    return a * int(b)

# Test cases
def test_add_numbers():
    assert add_numbers(1, 2) == 3

def test_add_numbers_type_error():
    with pytest.raises(TypeError):
        add_numbers(1, "two")

def test_add_strings_type_error():
    with pytest.raises(TypeError):
        add_strings("hello", "world")

def test_process_value_int():
    assert process_value(10) == 10

def test_process_value_str():
    assert process_value("test") == "test"

def test_process_value_type_error():
    with pytest.raises(TypeError):
        process_value(10.5)

def test_sum_elements():
    assert sum_elements([1, 2, 3]) == 6

def test_sum_elements_type_error():
    with pytest.raises(TypeError):
        sum_elements([1, "2", 3])

def test_get_coordinates():
    assert get_coordinates() == (10, 20)

def test_multiply_numbers():
    assert multiply_numbers(3, '4') == 12

