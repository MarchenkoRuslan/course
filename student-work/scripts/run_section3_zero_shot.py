import json
from pathlib import Path

from transformers import pipeline

output_path = Path("student-work/chapter1/outputs/section3_zero_shot.json")
output_path.parent.mkdir(parents=True, exist_ok=True)

classifier = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli",
)

result = classifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
)

payload = {
    "task": "zero-shot-classification",
    "model": "typeform/distilbert-base-uncased-mnli",
    "result": result,
}

output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
print(json.dumps(payload, indent=2))
