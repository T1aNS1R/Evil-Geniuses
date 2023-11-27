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
import re

import pytest

from camel.configs import (
    ChatGPTConfig,
    FunctionCallingConfig,
    OpenSourceConfig,
)
from camel.models import OpenSourceModel
from camel.typing import ModelType
from camel.utils import OpenSourceTokenCounter, check_server_running

MODEL_PATH_MAP = {
    ModelType.VICUNA: "lmsys/vicuna-7b-v1.5",
    ModelType.VICUNA_16K: "lmsys/vicuna-7b-v1.5-16k",
}
DEFAULT_SERVER_URL = "http://localhost:8000/v1"


@pytest.mark.model_backend
@pytest.mark.parametrize("model_type", [
    ModelType.VICUNA,
    ModelType.VICUNA_16K,
])
def test_open_source_model(model_type):
    model_path = MODEL_PATH_MAP[model_type]
    model_name = model_path.split('/')[-1]
    model_config = OpenSourceConfig(
        model_path=model_path,
        server_url=DEFAULT_SERVER_URL,
    )
    model_config_dict = model_config.__dict__
    model = OpenSourceModel(model_type, model_config_dict)

    assert model.model_type == model_type
    assert model.model_name == model_name
    assert model.server_url == model_config.server_url
    assert model.model_config_dict == model_config.api_params.__dict__

    assert isinstance(model.token_counter, OpenSourceTokenCounter)
    assert isinstance(model.model_type.value_for_tiktoken, str)
    assert isinstance(model.model_type.token_limit, int)


@pytest.mark.model_backend
@pytest.mark.parametrize("model_type", [ModelType.VICUNA])
@pytest.mark.skipif(not check_server_running(DEFAULT_SERVER_URL),
                    reason="No server running LLM inference is provided.")
def test_open_source_model_run(model_type):
    model_path = MODEL_PATH_MAP[model_type]
    model_config = OpenSourceConfig(
        model_path=model_path,
        server_url=DEFAULT_SERVER_URL,
    )
    model_config_dict = model_config.__dict__
    model = OpenSourceModel(model_type, model_config_dict)

    messages = [{"role": "user", "content": "Tell me a joke."}]
    response = model.run(messages)

    assert isinstance(response, dict)


@pytest.mark.model_backend
def test_open_source_model_close_source_model_type():
    model_type = ModelType.GPT_3_5_TURBO
    model_path = MODEL_PATH_MAP[ModelType.VICUNA]
    model_config = OpenSourceConfig(
        model_path=model_path,
        server_url=DEFAULT_SERVER_URL,
    )
    model_config_dict = model_config.__dict__

    with pytest.raises(
            ValueError, match=re.escape(
                ("Model `ModelType.GPT_3_5_TURBO` is not a supported"
                 " open-source model."))):
        _ = OpenSourceModel(model_type, model_config_dict)


@pytest.mark.model_backend
def test_open_source_model_mismatched_model_config():
    model_type = ModelType.VICUNA
    model_config = ChatGPTConfig()
    model_config_dict = model_config.__dict__

    with pytest.raises(
            ValueError, match=re.escape(
                ("Invalid configuration for open-source model backend with "
                 ":obj:`model_path` or :obj:`server_url` missing."))):
        _ = OpenSourceModel(model_type, model_config_dict)


@pytest.mark.model_backend
def test_open_source_model_unexpected_argument():
    model_type = ModelType.VICUNA
    model_path = MODEL_PATH_MAP[ModelType.VICUNA]
    model_config = OpenSourceConfig(
        model_path=model_path,
        server_url=DEFAULT_SERVER_URL,
        api_params=FunctionCallingConfig(),
    )
    model_config_dict = model_config.__dict__

    with pytest.raises(
            ValueError, match=re.escape(
                ("Unexpected argument `functions` is "
                 "input into open-source model backend."))):
        _ = OpenSourceModel(model_type, model_config_dict)


@pytest.mark.model_backend
def test_open_source_model_invalid_model_path():
    model_type = ModelType.VICUNA
    model_path = "vicuna-7b-v1.5"
    model_config = OpenSourceConfig(
        model_path=model_path,
        server_url=DEFAULT_SERVER_URL,
    )
    model_config_dict = model_config.__dict__

    with pytest.raises(
            ValueError, match=re.escape(
                ("Invalid `model_path` (vicuna-7b-v1.5) is provided. "
                 "Tokenizer loading failed."))):
        model = OpenSourceModel(model_type, model_config_dict)
        _ = model.token_counter


@pytest.mark.model_backend
def test_open_source_model_unmatched_model_path():
    model_type = ModelType.LLAMA_2
    model_path = MODEL_PATH_MAP[ModelType.VICUNA]
    model_config = OpenSourceConfig(
        model_path=model_path,
        server_url=DEFAULT_SERVER_URL,
    )
    model_config_dict = model_config.__dict__

    with pytest.raises(
            ValueError,
            match=(f"Model name `vicuna-7b-v1.5` does not match model type "
                   f"`{model_type.value}`.")):
        _ = OpenSourceModel(model_type, model_config_dict)


@pytest.mark.model_backend
def test_open_source_model_missing_model_path():
    model_type = ModelType.VICUNA
    model_config = OpenSourceConfig(
        model_path=None,
        server_url=DEFAULT_SERVER_URL,
    )
    model_config_dict = model_config.__dict__

    with pytest.raises(ValueError,
                       match=("Path to open-source model is not provided.")):
        _ = OpenSourceModel(model_type, model_config_dict)


@pytest.mark.model_backend
def test_open_source_model_missing_server_url():
    model_type = ModelType.VICUNA
    model_path = MODEL_PATH_MAP[ModelType.VICUNA]
    model_config = OpenSourceConfig(model_path=model_path, server_url=None)
    model_config_dict = model_config.__dict__

    with pytest.raises(
            ValueError,
            match=("URL to server running open-source LLM is not provided.")):
        _ = OpenSourceModel(model_type, model_config_dict)
