import json
from pathlib import Path

from transformers import pipeline

output_path = Path("student-work/chapter1/outputs/section3_sentiment.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

classifier = pipeline("sentiment-analysis")

single_result = classifier("I've been waiting for a HuggingFace course my whole life.")
batch_result = classifier(
    ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
)

payload = {
    "task": "sentiment-analysis",
    "single_result": single_result,
    "batch_result": batch_result,
}

output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(json.dumps(payload, indent=2))
