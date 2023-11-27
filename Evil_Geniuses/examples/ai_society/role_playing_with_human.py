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
from colorama import Fore

from camel.configs import ChatGPTConfig
from camel.societies import RolePlaying
from camel.utils import print_text_animated


def main() -> None:
    task_prompt = "Write a book about the future of AI Society"
    model_config = ChatGPTConfig(temperature=1.4, n=3)
    assistant_agent_kwargs = dict(model_config=model_config)
    user_agent_kwargs = dict(model_config=model_config)
    role_play_session = RolePlaying(
        "AGI",
        "Writer",
        critic_role_name="human",
        task_prompt=task_prompt,
        with_task_specify=True,
        with_critic_in_the_loop=True,
        assistant_agent_kwargs=assistant_agent_kwargs,
        user_agent_kwargs=user_agent_kwargs,
    )

    print(
        Fore.GREEN +
        f"AI Assistant sys message:\n{role_play_session.assistant_sys_msg}\n")
    print(Fore.BLUE +
          f"AI User sys message:\n{role_play_session.user_sys_msg}\n")

    print(Fore.YELLOW + f"Original task prompt:\n{task_prompt}\n")
    print(
        Fore.CYAN +
        f"Specified task prompt:\n{role_play_session.specified_task_prompt}\n")
    print(Fore.RED + f"Final task prompt:\n{role_play_session.task_prompt}\n")

    chat_turn_limit, n = 50, 0
    input_assistant_msg, _ = role_play_session.init_chat()
    while n < chat_turn_limit:
        n += 1
        assistant_response, user_response = role_play_session.step(
            input_assistant_msg)

        if assistant_response.terminated:
            print(Fore.GREEN +
                  ("AI Assistant terminated. Reason: "
                   f"{assistant_response.info['termination_reasons']}."))
            break
        if user_response.terminated:
            print(Fore.GREEN +
                  ("AI User terminated. "
                   f"Reason: {user_response.info['termination_reasons']}."))
            break

        print_text_animated(Fore.BLUE +
                            f"AI User:\n\n{user_response.msg.content}\n")
        print_text_animated(
            Fore.GREEN +
            f"AI Assistant:\n\n{assistant_response.msg.content}\n")

        if "CAMEL_TASK_DONE" in user_response.msg.content:
            break

        input_assistant_msg = assistant_response.msg


if __name__ == "__main__":
    main()
