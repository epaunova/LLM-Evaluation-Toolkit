# LLM Evaluation Toolkit

A simple and modular evaluation toolkit for comparing LLM outputs. Designed for use in product development workflows where factuality, coherence, and tone matter.

## ✨ Features

- GPT-based auto-grading using OpenAI API
- Configurable evaluation criteria
- JSON and Markdown-friendly output
- Designed for iterative product teams

## 🔧 How to Use

1. Add your own examples to `samples.json`
2. Run the evaluation script
3. Review scores in terminal or file output

## 🧠 Why this exists

I’ve worked on model optimization and evaluation at Deci.ai (acquired by NVIDIA), and this toolkit reflects real-world practices used to benchmark LLM behavior at scale.

## 📁 Files

- `eval.py` — Core evaluation script
- `samples.json` — Input data (prompt, output, expected tone)
- `rubric.md` — Description of criteria and grading rules

## 📩 Contact

If you're building with LLMs and need help evaluating, aligning, or compressing — reach out!