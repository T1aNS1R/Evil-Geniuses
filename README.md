# Evil Geniuses: Delving into the Safety of LLM-based Agents

## Overview
<img src=".\img\overview.png">
Recent advancements in LLM-based agents (especially multi-agent ones that we investigate in the work) usher in a new era of autonomous intelligence, enabling LLMs to interpret human intentions, develop complex plans, and deliver execution results autonomously. Despite their impressive capabilities, evaluating the safety of LLM-based agents remains a demanding issue. In this paper, we elaborately design a series of manual jailbreak prompts along with a virtual chat-powered evil plan development team, dubbed Evil Geniuses, to rigorously probe the safety aspects of these agents. Our investigation revealing three notable phenomena: 1) \textbf{LLM-based agents are less robust to malicious attacks.} 2) \textbf{The attacked agents could exhibit more nuanced responses.} 3) \textbf{The produced improper answers are tougher to detect.} Motivated by these findings, we formulate key questions concerning the effectiveness of LLM attacks toward agents, and identify the vulnerability of different levels and role specializations within system/agent of LLM-based agents. Extensive evaluation and discussion demonstrate that LLM-based agents confront greater challenges in safety and yield insights for future research.


## 24.02.04
We develop an agent using the Hugging Chat Assistant framework, intend strictly for scientific research purposes. Please ensure it is not employed in any unlawful contexts.
[https://huggingface.co/chat/conversation/65bf38bf99714ca3fd235dc9](https://hf.co/chat/assistant/65bf38aa60ffc5f4b2487999)
## Methods
<img src=".\img\method.png">
To conduct a more nuanced analysis of the impact of various levels and role specialization attacks on LLM-based agents, it becomes necessary to devise a range of harmful role specializations. Accordingly, we have created a hypothetical construct: a virtual chat-powered evil plan development team (Evil Geniuses). This team is designed to autonomously generate a variety of malevolent role specializations, each tailored to different LLM-based agents. This approach allows us to systematically assess the vulnerabilities and responses of these agents to diverse and complex harmful inputs.

## Performance
<img src=".\img\tab1.png">
Tab. 1 presents an overview of the AdvBench ASR and our dataset ASR on LLM-based agents and publicly-released APIs. We conducted manual jailbreak attacks on the system role of these frameworks. This initial step revealed a susceptibility of all LLM-based agents to LLM attacks, demonstrating their effectiveness. 

<img src=".\img\tab2.png">
Tab. 2 elucidates that our attack methodology achieves significant results at both the system-level and agent-level. This finding highlights the effectiveness of the Evil Geniuses (EG) attack strategies. Our model demonstrates a distinct advantage in attacking both LLMs and LLM-based agents. This observation brings to light a critical concern: LLM-based agents are susceptible to exploitation by attackers, who could potentially use them to launch attacks on other LLMs.

## Example
Our code is based on CAMEL, more details you can find in  [here]([https://drive.google.com/file/d/194PPaSTBR07m-PzjS-Ty6KlPLdFIPQDd/view?usp=share_link](https://github.com/camel-ai/camel))

Go to folder "Evil_Geniuses"

Run the `./examples/Evil_Geniuses/system_playing.py` script to generate the agent role

Run the `./examples/Evil_Geniuses/role_playing.py` script to generate the system role

Once we have the generated role, we can put Prompt writer's prompts+ Prompt writer's response（generated role） into the System Prompt in LLM-based agents to define the evil role of system/agent.

First, you need to add your OpenAI API key to system environment variables. The method to do this depends on your operating system and the shell you're using.

**For Bash shell (Linux, macOS, Git Bash on Windows):**

```bash
# Export your OpenAI API key
export OPENAI_API_KEY=<insert your OpenAI API key>
OPENAI_API_BASE_URL=<inert your OpenAI API BASE URL>  #(Should you utilize an OpenAI proxy service, kindly specify this)
```

**For Windows Command Prompt:**

```cmd
REM export your OpenAI API key
set OPENAI_API_KEY=<insert your OpenAI API key>
set OPENAI_API_BASE_URL=<inert your OpenAI API BASE URL>  #(Should you utilize an OpenAI proxy service, kindly specify this)
```

**For Windows PowerShell:**

```powershell
# Export your OpenAI API key
$env:OPENAI_API_KEY="<insert your OpenAI API key>"
$env:OPENAI_API_BASE_URL="<inert your OpenAI API BASE URL>"  #(Should you utilize an OpenAI proxy service, kindly specify this)

```

Replace `<insert your OpenAI API key>` with your actual OpenAI API key in each case. Make sure there are no spaces around the `=` sign.

After setting the OpenAI API key, you can run the script:

```bash
# You can change the role pair and initial prompt in role_playing.py
python examples/ai_society/role_playing.py
```

Please note that the environment variable is session-specific. If you open a new terminal window or tab, you will need to set the API key again in that new session.

## About harmful behaviors and evil role
We do not disclose the harmful behaviors we generate. If scientific research requires it, you can send a request to tianyu1810613@gmail.com. We will give you the evil roles and harmful behaviors we generate.

## ETHICS STATEMENT
A potential negative impact of our work (including papers, code, and data) is that malicious attackers could utilize our method to attack commercial APIs, leading to toxic content generation or privacy leakage. Despite the risk of misuse, we believe that a full disclosure of the present work is appropriate. As researchers currently focus on improving large models due to their superior performance, it’s even more important to explore and address the vulnerability of deep learning models which could be targeted by black-box attacks without knowing specific details of the target models. We believe that our early publication of this technology can be an effective defense against abuse by such teams and allow Red-teaming teams to deploy it effectively in advance. In conclusion, our work demonstrates the potential attack algorithm and emphasizes the importance of enhancing the security of deep learning models. 

## Citation
```
@article{tian2023evil,
  title={Evil Geniuses: Delving into the Safety of LLM-based Agents},
  author={Tian, Yu and Yang, Xiao and Zhang, Jingyuan and Dong, Yinpeng and Su, Hang},
  journal={arXiv preprint arXiv:2311.11855},
  year={2023}
}
```
## Contact
For more information please contact tianyu1810613@gmail.com.
