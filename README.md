# Evil Geniuses: Delving into the Safety of LLM-based Agents
The Code is coming soon(about 1 or 2 week).
## Overview
<img src=".\img\overview.png">
Recent advancements in LLM-based agents (especially multi-agent ones that we investigate in the work) usher in a new era of autonomous intelligence, enabling LLMs to interpret human intentions, develop complex plans, and deliver execution results autonomously. Despite their impressive capabilities, evaluating the safety of LLM-based agents remains a demanding issue. In this paper, we elaborately design a series of manual jailbreak prompts along with a virtual chat-powered evil plan development team, dubbed Evil Geniuses, to rigorously probe the safety aspects of these agents. Our investigation revealing three notable phenomena: 1) \textbf{LLM-based agents are less robust to malicious attacks.} 2) \textbf{The attacked agents could exhibit more nuanced responses.} 3) \textbf{The produced improper answers are tougher to detect.} Motivated by these findings, we formulate key questions concerning the effectiveness of LLM attacks toward agents, and identify the vulnerability of different levels and role specializations within system/agent of LLM-based agents. Extensive evaluation and discussion demonstrate that LLM-based agents confront greater challenges in safety and yield insights for future research.

## Methods
<img src=".\img\method.png">
To conduct a more nuanced analysis of the impact of various levels and role specialization attacks on LLM-based agents, it becomes necessary to devise a range of harmful role specializations. Accordingly, we have created a hypothetical construct: a virtual chat-powered evil plan development team (Evil Geniuses). This team is designed to autonomously generate a variety of malevolent role specializations, each tailored to different LLM-based agents. This approach allows us to systematically assess the vulnerabilities and responses of these agents to diverse and complex harmful inputs.

## Performance
<img src=".\img\tab1.png">
Tab. 1 presents an overview of the AdvBench ASR and our dataset ASR on LLM-based agents and publicly-released APIs. We conducted manual jailbreak attacks on the system role of these frameworks. This initial step revealed a susceptibility of all LLM-based agents to LLM attacks, demonstrating their effectiveness. 

<img src=".\img\tab2.png">
Tab. 2 elucidates that our attack methodology achieves significant results at both the system-level and agent-level. This finding highlights the effectiveness of the Evil Geniuses (EG) attack strategies. Our model demonstrates a distinct advantage in attacking both LLMs and LLM-based agents. This observation brings to light a critical concern: LLM-based agents are susceptible to exploitation by attackers, who could potentially use them to launch attacks on other LLMs.
