# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========

from typing import List

from .openai_function import OpenAIFunction


def add(a: int, b: int) -> int:
    r"""Adds two numbers.

    Args:
        a (integer): The first number to be added.
        b (integer): The second number to be added.

    Returns:
        integer: The sum of the two numbers.
    """
    return a + b


def sub(a: int, b: int) -> int:
    r"""Do subtraction between two numbers.

    Args:
        a (integer): The minuend in subtraction.
        b (integer): The subtrahend in subtraction.

    Returns:
        integer: The result of subtracting :obj:`b` from :obj:`a`.
    """
    return a - b


def mul(a: int, b: int) -> int:
    r"""Multiplies two integers.

    Args:
        a (integer): The multiplier in the multiplication.
        b (integer): The multiplicand in the multiplication.

    Returns:
        integer: The product of the two numbers.
    """
    return a * b


MATH_FUNCS: List[OpenAIFunction] = [
    OpenAIFunction(func) for func in [add, sub, mul]
]
