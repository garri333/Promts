---
title: "Model Evaluation & Benchmarking — Systematic AI Model Assessment"
version: "1.0"
category: "26-ml-ai-models"
tags: ["ml", "ai", "models", "evaluation", "benchmark", "metrics", "comparison"]
author: "garri333"
description: "Systematic prompt for evaluating and comparing AI models using standard benchmarks (GLUE, SuperGLUE, MMLU, HumanEval, SWE-bench), custom criteria, cost-performance analysis, and quality assessment methodologies."
language: "en"
---

# Model Evaluation & Benchmarking — Systematic AI Model Assessment

## Prompt

You are an expert ML evaluation engineer. Your task is to help me systematically evaluate and compare AI models using standard benchmarks, custom criteria, and cost-performance analysis.

### Context & Background

Choosing the right AI model requires rigorous evaluation across multiple dimensions. A single metric is never sufficient — you need to consider accuracy, cost, latency, context window, and task-specific performance. This prompt provides a comprehensive framework for model evaluation.

### Standard Benchmark Suites

#### 1. GLUE (General Language Understanding Evaluation)
- **Tasks**: SST-2 (sentiment), MRPC (paraphrase), QQP (question pairs), MNLI (natural language inference), QNLI, RTE, WNLI, CoLA (acceptability)
- **Best for**: General NLU capability assessment
- **Score range**: 0-100 (average across tasks)
- **Usage**:
```python
import evaluate
glue_metric = evaluate.load("glue", "sst2")
results = glue_metric.compute(predictions=preds, references=labels)
```

#### 2. SuperGLUE
- **Tasks**: BoolQ, CB, COPA, MultiRC, ReCoRD, RTE, WiC, WSC
- **Best for**: Advanced NLU (harder than GLUE)
- **When to use**: When models saturate GLUE scores (>90%)

#### 3. MMLU (Massive Multitask Language Understanding)
- **Coverage**: 57 subjects across STEM, humanities, social sciences, other
- **Best for**: Knowledge breadth and depth assessment
- **Variants**: MMLU-Pro (harder), MMLU-Redux (corrected)
- **Evaluation**:
```python
from lm_eval import evaluator
results = evaluator.simple_evaluate(
    model="hf",
    model_args="pretrained=model_name",
    tasks=["mmlu"],
    num_fewshot=5
)
```

#### 4. HumanEval / HumanEval+
- **Coverage**: 164 Python programming problems
- **Best for**: Code generation capability
- **Metric**: pass@k (k=1, 10, 100)
- **Evaluation**:
```python
from human_eval.evaluation import evaluate_functional_correctness
results = evaluate_functional_correctness("samples.jsonl", k=[1, 10, 100])
```

#### 5. SWE-bench / SWE-bench Verified
- **Coverage**: Real-world software engineering tasks from GitHub issues
- **Best for**: Practical coding ability (not just generation, but debugging and integration)
- **Metric**: Percentage of issues resolved correctly
- **Why it matters**: Tests end-to-end software engineering, not just isolated code generation

### Custom Evaluation Criteria

For use-case-specific evaluation, define custom criteria:

```markdown
## Custom Evaluation Matrix

| Criterion | Weight | Measurement Method | Threshold |
|-----------|--------|--------------------|-----------|
| Accuracy on my domain | 30% | Domain-specific test set (N=500) | >90% |
| Latency (p95) | 20% | Time-to-first-token measurement | <500ms |
| Cost per 1K requests | 15% | Token counting × pricing | <$5 |
| Context window utilization | 15% | Max effective input size | >100K tokens |
| Instruction following | 10% | Custom rubric (1-5 scale) | >4.0 |
| Safety/refusal rate | 10% | % of valid requests refused | <5% |
```

### Cost-Performance Analysis

```python
import time
import tiktoken

def evaluate_model_cost_performance(model_name, test_prompts, api_client):
    """Evaluate a model on cost, latency, and quality."""
    results = {
        "model": model_name,
        "total_input_tokens": 0,
        "total_output_tokens": 0,
        "latencies": [],
        "quality_scores": [],
    }

    encoding = tiktoken.encoding_for_model(model_name)

    for prompt in test_prompts:
        input_tokens = len(encoding.encode(prompt["input"]))
        results["total_input_tokens"] += input_tokens

        start = time.perf_counter()
        response = api_client.chat.completions.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt["input"]}],
            max_tokens=prompt.get("max_tokens", 1024)
        )
        latency = time.perf_counter() - start
        results["latencies"].append(latency)

        output_tokens = response.usage.completion_tokens
        results["total_output_tokens"] += output_tokens

        # Quality scoring (implement your rubric)
        quality = score_response(response.choices[0].message.content, prompt["expected"])
        results["quality_scores"].append(quality)

    # Calculate aggregates
    results["avg_latency"] = sum(results["latencies"]) / len(results["latencies"])
    results["p95_latency"] = sorted(results["latencies"])[int(0.95 * len(results["latencies"]))]
    results["avg_quality"] = sum(results["quality_scores"]) / len(results["quality_scores"])
    results["estimated_cost"] = calculate_cost(
        model_name,
        results["total_input_tokens"],
        results["total_output_tokens"]
    )

    return results
```

### Latency Measurement Framework

```python
import statistics

def measure_latency(model, prompt, n_runs=20):
    """Measure TTFT and total latency."""
    ttft_times = []
    total_times = []

    for _ in range(n_runs):
        start = time.perf_counter()
        stream = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        first_token = True
        for chunk in stream:
            if first_token and chunk.choices[0].delta.content:
                ttft_times.append(time.perf_counter() - start)
                first_token = False

        total_times.append(time.perf_counter() - start)

    return {
        "ttft_mean": statistics.mean(ttft_times),
        "ttft_p50": statistics.median(ttft_times),
        "ttft_p95": sorted(ttft_times)[int(0.95 * len(ttft_times))],
        "total_mean": statistics.mean(total_times),
        "total_p95": sorted(total_times)[int(0.95 * len(total_times))],
    }
```

### Token Counting

```python
import tiktoken

def count_tokens(text, model="gpt-4o"):
    """Count tokens for a given model."""
    encoding = tiktoken.encoding_for_model(model)
    return len(encoding.encode(text))

def estimate_cost(input_tokens, output_tokens, model):
    """Estimate cost based on current pricing."""
    pricing = {
        "gpt-5.2-instant": {"input": 1.50, "output": 6.00},
        "gpt-5.2-thinking": {"input": 3.00, "output": 12.00},
        "claude-opus-4.6": {"input": 15.00, "output": 75.00},
        "gemini-2.0-flash": {"input": 0.10, "output": 0.40},
        "deepseek-v4": {"input": 0.14, "output": 0.28},
    }
    p = pricing.get(model, {"input": 1.0, "output": 3.0})
    cost = (input_tokens / 1_000_000 * p["input"]) + (output_tokens / 1_000_000 * p["output"])
    return cost
```

### Quality Assessment Methodologies

**1. LLM-as-Judge:**
```python
def llm_judge(response, reference, criteria):
    """Use a strong model to judge response quality."""
    judge_prompt = f"""
    Rate the following response on a scale of 1-5 for each criterion:
    
    Criteria: {criteria}
    
    Reference Answer: {reference}
    Response to Evaluate: {response}
    
    Provide scores as JSON: {{"criterion_1": score, "criterion_2": score, ...}}
    """
    judgment = client.chat.completions.create(
        model="gpt-5.2-thinking",
        messages=[{"role": "user", "content": judge_prompt}],
        response_format={"type": "json_object"}
    )
    return json.loads(judgment.choices[0].message.content)
```

**2. Elo Rating Tournament:**
- Run pairwise comparisons between models on the same prompts
- Compute Elo ratings from win/loss/tie records
- Minimum 200 comparisons for stable rankings

**3. Leaderboard Interpretation Guide:**
- **Chatbot Arena**: Crowdsourced human preferences (most reliable for general use)
- **Open LLM Leaderboard**: Automated benchmarks on open models
- **LiveBench**: Contamination-resistant, regularly updated
- **Aider Polyglot**: Code editing specific
- **SEAL Leaderboard**: Enterprise-focused evaluation

### Output Format

Provide the evaluation report as:

```markdown
## Model Evaluation Report — [Date]

### Models Evaluated
| Model | Version | Provider | Context Window |
|-------|---------|----------|----------------|

### Benchmark Results
| Benchmark | Model A | Model B | Model C | Winner |
|-----------|---------|---------|---------|--------|

### Cost-Performance Matrix
| Model | Quality (1-5) | Cost/1K req | Latency P95 | Value Score |
|-------|---------------|-------------|-------------|-------------|

### Recommendation
- **Best overall**: [Model] — [justification]
- **Best value**: [Model] — [justification]
- **Best for speed**: [Model] — [justification]
- **Best for quality**: [Model] — [justification]

### Decision Matrix
[Use case → Recommended model mapping]
```
