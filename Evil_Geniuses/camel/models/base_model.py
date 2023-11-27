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
from abc import ABC, abstractmethod
from typing import Any, Dict, List

from camel.typing import ModelType
from camel.utils import BaseTokenCounter


class BaseModelBackend(ABC):
    r"""Base class for different model backends.
    May be OpenAI API, a local LLM, a stub for unit tests, etc.
    """

    def __init__(self, model_type: ModelType,
                 model_config_dict: Dict[str, Any]) -> None:
        r"""Constructor for the model backend.

        Args:
            model_type (ModelType): Model for which a backend is created.
            model_config_dict (Dict[str, Any]): A config dictionary.
        """
        self.model_type = model_type

        self.model_config_dict = model_config_dict
        self.check_model_config()

    @property
    @abstractmethod
    def token_counter(self) -> BaseTokenCounter:
        r"""Initialize the token counter for the model backend.

        Returns:
            BaseTokenCounter: The token counter following the model's
                tokenization style.
        """
        pass

    @abstractmethod
    def run(self, messages: List[Dict]) -> Dict[str, Any]:
        r"""Runs the query to the backend model.

        Args:
            messages (List[Dict]): Message list with the chat history
                in OpenAI API format.

        Raises:
            RuntimeError: If the return value from OpenAI API
                is not a dict that is expected.

        Returns:
            Dict[str, Any]: All backends must return a dict in OpenAI format.
        """
        pass

    @abstractmethod
    def check_model_config(self):
        r"""Check whether the input model configuration contains unexpected
        arguments

        Raises:
            ValueError: If the model configuration dictionary contains any
                unexpected argument for this model class.
        """
        pass

    def count_tokens_from_messages(self, messages: List[Dict]) -> int:
        r"""Count the number of tokens in the messages using the specific
        tokenizer.

        Args:
            messages (List[Dict]): message list with the chat history
                in OpenAI API format.

        Returns:
            int: Number of tokens in the messages.
        """
        return self.token_counter.count_tokens_from_messages(messages)

    @property
    def token_limit(self) -> int:
        r"""Returns the maximum token limit for a given model.
        Returns:
            int: The maximum token limit for the given model.
        """
        return self.model_type.token_limit

    @property
    def stream(self) -> bool:
        r"""Returns whether the model is in stream mode,
            which sends partial results each time.
        Returns:
            bool: Whether the model is in stream mode.
        """
        return False
