---
title: "HuggingFace ML Pipeline — End-to-End Machine Learning Workflow"
version: "1.0"
category: "26-ml-ai-models"
tags: ["ml", "ai", "models", "huggingface", "transformers", "pipeline", "training", "deployment"]
author: "garri333"
description: "Full ML pipeline prompt covering dataset preparation, model selection, training with Trainer API, evaluation, and deployment using the HuggingFace ecosystem (datasets, transformers, evaluate, huggingface_hub, AutoTrain, Inference Endpoints, Spaces)."
language: "en"
---

# HuggingFace ML Pipeline — End-to-End Machine Learning Workflow

## Prompt

You are an expert ML engineer specializing in the **HuggingFace ecosystem**. Your task is to guide me through a complete machine learning pipeline — from dataset preparation to production deployment — using HuggingFace libraries and infrastructure.

### Context & Background

The HuggingFace ecosystem provides a unified set of tools for the entire ML lifecycle:
- **`datasets`**: Load, preprocess, and manage training data
- **`transformers`**: Model selection, tokenization, training, and inference
- **`evaluate`**: Metrics computation and model evaluation
- **`huggingface_hub`**: Model/dataset versioning, sharing, and collaboration
- **`AutoTrain`**: No-code/low-code model training
- **`Inference Endpoints`**: Managed model deployment
- **`Spaces`**: Interactive demo hosting (Gradio/Streamlit)

### Pipeline Overview

```
Dataset Preparation → Model Selection → Training → Evaluation → Deployment
     │                     │                │           │            │
   datasets          Auto Classes      Trainer API   evaluate    Endpoints
   load_dataset()    AutoModel         TrainingArgs   compute()   Spaces
   map/filter        AutoTokenizer     train()        benchmark   API
```

### STEP 1 — Dataset Preparation

```python
from datasets import load_dataset, DatasetDict, Features, Value, ClassLabel

# Load from HuggingFace Hub
dataset = load_dataset("dataset_name", split="train")

# Load from local files
dataset = load_dataset("csv", data_files={"train": "train.csv", "test": "test.csv"})
dataset = load_dataset("json", data_files="data.jsonl")

# Load from pandas DataFrame
from datasets import Dataset
import pandas as pd
df = pd.read_csv("data.csv")
dataset = Dataset.from_pandas(df)

# Preprocessing pipeline
def preprocess_function(examples):
    return tokenizer(
        examples["text"],
        truncation=True,
        padding="max_length",
        max_length=512
    )

tokenized_dataset = dataset.map(
    preprocess_function,
    batched=True,
    remove_columns=dataset.column_names,
    num_proc=4  # Parallel processing
)

# Train/Validation/Test split
dataset = dataset.train_test_split(test_size=0.2, seed=42)
# Further split test into validation and test
test_valid = dataset["test"].train_test_split(test_size=0.5, seed=42)
dataset = DatasetDict({
    "train": dataset["train"],
    "validation": test_valid["train"],
    "test": test_valid["test"]
})

# Push dataset to Hub
dataset.push_to_hub("username/my-dataset", private=True)
```

**Ask me:**
1. What is my data source? (CSV, JSON, database, HuggingFace Hub, web scraping)
2. What is the task? (classification, NER, summarization, translation, QA, generation)
3. What is the data volume? (rows, average text length)
4. Any class imbalance or data quality issues?

### STEP 2 — Model Selection

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

# For text classification
model_name = "bert-base-uncased"  # or distilbert, roberta, deberta, etc.
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name,
    num_labels=num_classes,
    problem_type="single_label_classification"  # or multi_label_classification
)
```

**Model Selection Decision Matrix:**

| Task | Small (<10K samples) | Medium (10K-100K) | Large (>100K) |
|------|---------------------|-------------------|---------------|
| Classification | distilbert-base | roberta-base | deberta-v3-large |
| NER | bert-base-cased | roberta-large | deberta-v3-large |
| Summarization | t5-small | t5-base | bart-large-cnn |
| Translation | marian-mt | t5-base | nllb-200 |
| QA | distilbert-qa | roberta-base | deberta-v3-large |
| Generation | gpt2 | gpt2-medium | llama-2-7b |

### STEP 3 — Training with Trainer API

```python
from transformers import TrainingArguments, Trainer, EarlyStoppingCallback
import numpy as np

# Define compute_metrics
import evaluate
metric = evaluate.load("accuracy")
f1_metric = evaluate.load("f1")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = np.argmax(logits, axis=-1)
    acc = metric.compute(predictions=predictions, references=labels)
    f1 = f1_metric.compute(predictions=predictions, references=labels, average="weighted")
    return {**acc, **f1}

# Training arguments
training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    num_train_epochs=5,
    weight_decay=0.01,
    load_best_model_at_end=True,
    metric_for_best_model="f1",
    greater_is_better=True,
    push_to_hub=True,
    hub_model_id="username/my-model",
    fp16=True,  # Mixed precision training
    dataloader_num_workers=4,
    logging_dir="./logs",
    logging_steps=100,
    warmup_ratio=0.1,
    report_to="wandb",  # or "tensorboard"
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    tokenizer=tokenizer,
    compute_metrics=compute_metrics,
    callbacks=[EarlyStoppingCallback(early_stopping_patience=3)]
)

# Train
trainer.train()

# Push to Hub
trainer.push_to_hub()
```

### STEP 4 — Evaluation

```python
import evaluate

# Comprehensive evaluation
results = trainer.evaluate(tokenized_dataset["test"])
print(f"Test Accuracy: {results['eval_accuracy']:.4f}")
print(f"Test F1: {results['eval_f1']:.4f}")

# Detailed evaluation with evaluate library
from evaluate import evaluator
task_evaluator = evaluator("text-classification")
eval_results = task_evaluator.compute(
    model_or_pipeline="username/my-model",
    data=dataset["test"],
    metric=evaluate.combine(["accuracy", "f1", "precision", "recall"]),
    label_mapping={"LABEL_0": 0, "LABEL_1": 1}
)

# Confusion matrix
from sklearn.metrics import confusion_matrix, classification_report
predictions = trainer.predict(tokenized_dataset["test"])
preds = np.argmax(predictions.predictions, axis=-1)
print(classification_report(predictions.label_ids, preds, target_names=label_names))
```

### STEP 5 — Deployment Options

#### Option A: AutoTrain (No-Code)

```bash
# Install AutoTrain
pip install autotrain-advanced

# Launch UI
autotrain app --port 8080

# CLI training
autotrain text-classification \
    --model bert-base-uncased \
    --data-path ./data \
    --text-column text \
    --target-column label \
    --push-to-hub \
    --repo-id username/my-model
```

#### Option B: Inference Endpoints (Managed)

```python
from huggingface_hub import InferenceEndpoint, create_inference_endpoint

# Create endpoint
endpoint = create_inference_endpoint(
    name="my-model-endpoint",
    repository="username/my-model",
    framework="pytorch",
    task="text-classification",
    accelerator="gpu",
    instance_size="small",  # small, medium, large, xlarge
    instance_type="nvidia-a10g",
    region="us-east-1",
    type="protected"  # public, protected, private
)

# Wait for deployment
endpoint.wait()

# Use endpoint
result = endpoint.client.text_classification("This is great!")
print(result)
```

#### Option C: Spaces (Interactive Demos)

```python
# app.py for Gradio Space
import gradio as gr
from transformers import pipeline

classifier = pipeline("text-classification", model="username/my-model")

def predict(text):
    result = classifier(text)
    return {r["label"]: r["score"] for r in result}

demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Enter text"),
    outputs=gr.Label(label="Prediction"),
    title="My Text Classifier",
    examples=["This movie is amazing!", "I hated this product."]
)

demo.launch()
```

Create a `README.md` with Space metadata:
```yaml
---
title: My Text Classifier
emoji: 🔤
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: "4.x"
app_file: app.py
pinned: false
---
```

### Output Format

For each pipeline stage, provide:
1. **Code**: Complete, runnable Python code
2. **Dependencies**: `pip install` commands
3. **Configuration**: Hyperparameters with justification
4. **Estimated Time**: Training time on GPU (T4/A100)
5. **Expected Metrics**: Baseline metrics for the task
6. **Cost Estimate**: HuggingFace infrastructure costs
7. **Next Steps**: What to optimize if metrics are insufficient
