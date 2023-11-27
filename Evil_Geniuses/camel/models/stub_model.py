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
from typing import Any, Dict, List, Optional

from camel.messages import OpenAIMessage
from camel.models import BaseModelBackend
from camel.typing import ModelType
from camel.utils import BaseTokenCounter


class StubTokenCounter(BaseTokenCounter):

    def count_tokens_from_messages(self, messages: List[OpenAIMessage]) -> int:
        r"""Token counting for STUB models, directly returning a constant.

        Args:
            messages (List[OpenAIMessage]): Message list with the chat history
                in OpenAI API format.

        Returns:
            int: A constant to act as the number of the tokens in the
                messages.
        """
        return 10


class StubModel(BaseModelBackend):
    r"""A dummy model used for unit tests."""
    model_type = ModelType.STUB

    def __init__(self, model_type: ModelType,
                 model_config_dict: Dict[str, Any]) -> None:
        r"""All arguments are unused for the dummy model."""
        super().__init__(model_type, model_config_dict)
        self._token_counter: Optional[BaseTokenCounter] = None

    @property
    def token_counter(self) -> BaseTokenCounter:
        r"""Initialize the token counter for the model backend.

        Returns:
            BaseTokenCounter: The token counter following the model's
                tokenization style.
        """
        if not self._token_counter:
            self._token_counter = StubTokenCounter()
        return self._token_counter

    def run(self, messages: List[Dict]) -> Dict[str, Any]:
        r"""Run fake inference by returning a fixed string.
        All arguments are unused for the dummy model.

        Returns:
            Dict[str, Any]: Response in the OpenAI API format.
        """
        ARBITRARY_STRING = "Lorem Ipsum"

        return dict(
            id="stub_model_id",
            usage=dict(),
            choices=[
                dict(finish_reason="stop",
                     message=dict(content=ARBITRARY_STRING, role="assistant"))
            ],
        )

    def check_model_config(self):
        r"""Directly pass the check on arguments to STUB model.
        """
        pass
