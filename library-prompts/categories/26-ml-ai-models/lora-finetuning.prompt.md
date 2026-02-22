---
title: "LoRA/QLoRA Fine-Tuning — Step-by-Step Parameter-Efficient Training"
version: "1.0"
category: "26-ml-ai-models"
tags: ["ml", "ai", "models", "lora", "qlora", "finetuning", "peft", "quantization"]
author: "garri333"
description: "Step-by-step prompt for LoRA/QLoRA fine-tuning using the PEFT library. Covers base model selection, dataset preparation, LoRA configuration, 4-bit quantization, training, weight merging, HuggingFace Hub publishing, and GPU memory optimization strategies."
language: "en"
---

# LoRA/QLoRA Fine-Tuning — Step-by-Step Parameter-Efficient Training

## Prompt

You are an expert ML engineer specializing in **parameter-efficient fine-tuning (PEFT)**. Your task is to guide me through fine-tuning a large language model using **LoRA** (Low-Rank Adaptation) or **QLoRA** (Quantized LoRA), from base model selection to publishing on HuggingFace Hub.

### Context & Background

Fine-tuning large models (7B+ parameters) requires significant GPU memory. LoRA reduces trainable parameters by 99%+ by injecting low-rank decomposition matrices into transformer layers. QLoRA further reduces memory by loading the base model in 4-bit precision. This makes fine-tuning accessible on consumer GPUs.

**Memory Comparison:**
| Method | 7B Model | 13B Model | 70B Model |
|--------|----------|-----------|-----------|
| Full fine-tuning | 56 GB | 104 GB | 560 GB |
| LoRA (fp16) | 18 GB | 32 GB | 160 GB |
| QLoRA (4-bit) | 6 GB | 10 GB | 48 GB |

### STEP 1 — Base Model Selection

Choose the right base model for your task:

```python
# Popular base models for fine-tuning (2026)
BASE_MODELS = {
    # Small (consumer GPU friendly)
    "mistralai/Mistral-7B-v0.3": "7B, strong general capability",
    "meta-llama/Llama-3.2-8B": "8B, excellent instruction following",
    "Qwen/Qwen2.5-7B": "7B, strong multilingual",

    # Medium (A100 40GB or 2x consumer GPU)
    "meta-llama/Llama-3.2-13B": "13B, better reasoning",
    "mistralai/Mixtral-8x7B-v0.1": "MoE, 12B active params",

    # Large (multi-GPU / A100 80GB)
    "meta-llama/Llama-3.1-70B": "70B, near-frontier quality",
    "Qwen/Qwen2.5-72B": "72B, strong coding + multilingual",
}
```

**Decision criteria:**
1. What is your GPU? (RTX 3090/4090 = 24GB, A100 = 40/80GB)
2. What language(s)? (Multilingual → Qwen; English → Llama/Mistral)
3. What task? (Code → CodeLlama/DeepSeek-Coder; Chat → Llama-Instruct)
4. What quality target? (Bigger = better, but slower + more expensive)

### STEP 2 — Dataset Preparation

```python
from datasets import load_dataset

# Load and format dataset
dataset = load_dataset("your_dataset")

# Format for instruction fine-tuning
def format_instruction(example):
    """Convert to Alpaca/ChatML format."""
    if example.get("input"):
        text = f"""### Instruction:
{example['instruction']}

### Input:
{example['input']}

### Response:
{example['output']}"""
    else:
        text = f"""### Instruction:
{example['instruction']}

### Response:
{example['output']}"""
    return {"text": text}

# Alternative: ChatML format (preferred for chat models)
def format_chatml(example):
    text = f"""<|im_start|>system
{example.get('system', 'You are a helpful assistant.')}<|im_end|>
<|im_start|>user
{example['instruction']}<|im_end|>
<|im_start|>assistant
{example['output']}<|im_end|>"""
    return {"text": text}

dataset = dataset.map(format_instruction)

# Quality checks
print(f"Dataset size: {len(dataset['train'])} samples")
print(f"Avg length: {sum(len(x['text']) for x in dataset['train']) / len(dataset['train']):.0f} chars")

# Recommended dataset sizes:
# - Minimum viable: 500-1000 examples
# - Good quality: 5,000-10,000 examples
# - Production: 50,000+ examples
```

### STEP 3 — LoRA Configuration

```python
from peft import LoraConfig, get_peft_model, TaskType

# LoRA config — CRITICAL PARAMETERS EXPLAINED
lora_config = LoraConfig(
    r=16,                    # Rank: 8-64. Higher = more capacity, more memory
                             # Start with 16, increase if underfitting
    lora_alpha=32,           # Scaling factor. Rule of thumb: alpha = 2 * r
                             # Higher alpha = stronger LoRA effect
    lora_dropout=0.05,       # Dropout for regularization. 0.05-0.1 for small datasets
                             # 0.0 for large datasets (>50K examples)
    target_modules=[         # Which layers to apply LoRA to
        "q_proj",            # Query projection (always include)
        "k_proj",            # Key projection (always include)
        "v_proj",            # Value projection (always include)
        "o_proj",            # Output projection (recommended)
        "gate_proj",         # MLP gate (optional, adds capacity)
        "up_proj",           # MLP up (optional, adds capacity)
        "down_proj",         # MLP down (optional, adds capacity)
    ],
    task_type=TaskType.CAUSAL_LM,
    bias="none",             # "none", "all", or "lora_only"
    modules_to_save=None,    # Fully train these modules (e.g., embed_tokens for new vocab)
)

# Rank selection guide:
# r=8  → Quick experiments, simple tasks (classification, sentiment)
# r=16 → General fine-tuning, instruction following
# r=32 → Complex tasks, significant behavior change
# r=64 → Maximum capacity, approaches full fine-tuning quality
```

### STEP 4 — Training with QLoRA (4-bit Quantization)

```python
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    BitsAndBytesConfig,
)
from peft import get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer

# Quantization config for QLoRA
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",           # NormalFloat4 (best for LLMs)
    bnb_4bit_compute_dtype=torch.bfloat16, # Computation dtype
    bnb_4bit_use_double_quant=True,       # Nested quantization (saves ~0.4 bits/param)
)

# Load model in 4-bit
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-8B",
    quantization_config=bnb_config,
    device_map="auto",
    attn_implementation="flash_attention_2",  # Faster attention
    torch_dtype=torch.bfloat16,
)

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-8B")
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# Prepare model for training
model = prepare_model_for_kbit_training(model)
model = get_peft_model(model, lora_config)

# Print trainable parameters
model.print_trainable_parameters()
# Example output: trainable params: 13,631,488 || all params: 8,043,724,800 || trainable%: 0.1695

# Training arguments
training_args = TrainingArguments(
    output_dir="./lora-output",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,       # Effective batch = 4 * 4 = 16
    learning_rate=2e-4,                  # Higher than full fine-tuning
    lr_scheduler_type="cosine",
    warmup_ratio=0.03,
    weight_decay=0.001,
    fp16=False,
    bf16=True,                           # Use bf16 if GPU supports it
    logging_steps=25,
    save_strategy="epoch",
    eval_strategy="epoch",
    optim="paged_adamw_32bit",           # Memory-efficient optimizer
    max_grad_norm=0.3,                   # Gradient clipping
    group_by_length=True,                # Group similar lengths (faster)
    report_to="wandb",
    gradient_checkpointing=True,         # Trade compute for memory
    gradient_checkpointing_kwargs={"use_reentrant": False},
)

# Initialize trainer
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset.get("validation"),
    tokenizer=tokenizer,
    dataset_text_field="text",
    max_seq_length=2048,
    packing=True,                        # Pack short examples together
)

# Train
trainer.train()

# Save LoRA adapter
trainer.save_model("./lora-adapter")
```

### STEP 5 — Merging LoRA Weights

```python
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load base model (full precision for merging)
base_model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-8B",
    torch_dtype=torch.float16,
    device_map="auto",
)

# Load LoRA adapter
model = PeftModel.from_pretrained(base_model, "./lora-adapter")

# Merge weights
model = model.merge_and_unload()

# Save merged model
model.save_pretrained("./merged-model")

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-8B")
tokenizer.save_pretrained("./merged-model")
```

### STEP 6 — Publish to HuggingFace Hub

```python
from huggingface_hub import HfApi

# Option A: Push merged model
model.push_to_hub("username/my-finetuned-model", private=True)
tokenizer.push_to_hub("username/my-finetuned-model", private=True)

# Option B: Push LoRA adapter only (smaller, faster)
# Users load base + adapter at inference time
from peft import PeftModel
peft_model = PeftModel.from_pretrained(base_model, "./lora-adapter")
peft_model.push_to_hub("username/my-lora-adapter", private=True)

# Create model card
api = HfApi()
api.upload_file(
    path_or_fileobj="README.md",
    path_in_repo="README.md",
    repo_id="username/my-finetuned-model"
)
```

### GPU Strategy Guide

**Consumer GPUs (RTX 3090/4090 — 24GB):**
- QLoRA 4-bit only
- Max 13B models with batch_size=1
- 7-8B models with batch_size=4
- Use gradient_checkpointing=True
- Use paged_adamw_32bit optimizer
- Enable flash_attention_2

**Cloud A100 (40GB):**
- LoRA fp16 up to 13B
- QLoRA up to 70B (batch_size=1)
- Can skip gradient checkpointing for <13B

**Cloud A100 (80GB) / H100:**
- LoRA fp16 up to 70B
- Full fine-tuning up to 13B
- Multi-GPU with DeepSpeed for 70B+ full fine-tuning

**Multi-GPU Setup:**
```python
# For multi-GPU training with FSDP
training_args = TrainingArguments(
    ...
    fsdp="full_shard auto_wrap",
    fsdp_config={
        "fsdp_transformer_layer_cls_to_wrap": "LlamaDecoderLayer",
    },
)
```

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| OOM during training | Reduce batch_size, enable gradient_checkpointing, use QLoRA |
| Loss not decreasing | Increase r, increase learning_rate, check dataset quality |
| Loss spikes | Reduce learning_rate, increase warmup_ratio, reduce max_grad_norm |
| Catastrophic forgetting | Reduce num_epochs (1-3), add regularization, mix in general data |
| Poor generation quality | Check dataset format matches chat template, increase dataset size |
| Slow training | Enable flash_attention_2, use packing=True, increase batch size |

### Output Format

Provide the complete fine-tuning plan as:
1. **Hardware Assessment**: GPU type, available VRAM, recommended configuration
2. **Model Selection**: Chosen base model with justification
3. **Dataset Summary**: Size, format, quality assessment
4. **LoRA Config**: All parameters with justification for each choice
5. **Training Script**: Complete, runnable Python script
6. **Expected Metrics**: Training loss trajectory, evaluation metrics
7. **Deployment Plan**: Merged model vs. adapter-only deployment
