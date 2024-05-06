import pytest
from .typechecking_decorator import typecheck
from typing import Union, Iterable, Tuple, Callable,  Awaitable, TypeVar
import typing as tp
import asyncio
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

@typecheck
def call_func(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

@typecheck
async def async_call_func(func: Awaitable[Callable[[int, int], int]], a: int, b: int) -> int:
    return await func(a, b)

T = TypeVar('T', bound=float)

@typecheck
def typevar_func(a: T, b: T) -> T:
    return a 




class Bla(tp._TypedDict):
    a: tp.List[int]
    b: str

@typecheck
def check_typed_dict(data: Bla) -> tp.List[int]:
    return data.get("a")

def test_check_typed_dict():
    # Create an instance of Bla with correct types
    bla_instance = Bla(a=[1, 2, 3], b="test")
    # Test the function with the instance
    assert check_typed_dict(bla_instance) == [1, 2, 3]


def test_test_typed_dict_type_error():
    with pytest.raises(TypeError):
        check_typed_dict(Bla(a="1", b="test"))

async def async_add_numbers(a: int, b: int) -> int:
    return a + b

def add_numbers(a: int, b: int) -> int:
    return a + b

def test_call_func():
    assert call_func(add_numbers, 1, 2) == 3

def test_call_func_type_error():
    def wrong_func(a: int, b: str) -> int:
        return a + int(b)

    with pytest.raises(TypeError):
        call_func(wrong_func, 1, 2)

def test_async_call_func():
    assert asyncio.run(async_call_func(async_add_numbers, 1, 2)) == 3

def test_async_call_func_type_error():
    async def wrong_func(a: int, b: str) -> int:
        return a + int(b)

    with pytest.raises(TypeError):
        asyncio.run(async_call_func(wrong_func, 1, 2))

# Test cases
def test_add_numbers_success():
    user1 = 1.0
    user2 = 2.0
    result = typevar_func(user1, user2)
    assert isinstance(result, float)

def test_add_numbers_type_mismatch():
    user = 1.0
    admin = "Charlie Parker"
    with pytest.raises(TypeError):
        typevar_func(user, admin)

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

