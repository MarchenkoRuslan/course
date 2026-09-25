# Chapter 1 Notes

## Section 3: Transformers, what can they do?

Goal: run the first `pipeline()` examples locally and keep a notebook with outputs that can be shown later.

Source lesson: https://huggingface.co/learn/llm-course/chapter1/3

Local working notebook:

```text
student-work/notebooks/chapter1/section3_pipelines.ipynb
```

## Checklist

- [x] Open the notebook locally in VS Code or Jupyter.
- [x] Run the install cell.
- [x] Run sentiment analysis.
- [x] Run zero-shot classification.
- [ ] Run text generation with `HuggingFaceTB/SmolLM2-360M`.
- [ ] Run fill-mask.
- [ ] Run named entity recognition.
- [ ] Run question answering.
- [ ] Run summarization.
- [ ] Run translation.
- [ ] Save outputs that are useful for the demo.

## Notes

- Runtime is using the `HF Course Local` kernel from `.venv`.
- Installed the minimal local runtime for this section: `torch`, `transformers[sentencepiece]`, `pillow`, and `soundfile`.
- The full `datasets evaluate transformers[sentencepiece]` install hung while installing `sympy`; splitting installs fixed the setup.
- Sentiment analysis uses the default model `distilbert/distilbert-base-uncased-finetuned-sst-2-english`.
- First model download cached about 268 MB of weights locally.
- Saved sentiment output to `student-work/chapter1/outputs/section3_sentiment.json`.
- Zero-shot classification uses the compact model `typeform/distilbert-base-uncased-mnli` instead of the larger default model.
- Zero-shot result still ranks `education` first for the course sentence, but with lower confidence than the course example.
- Saved zero-shot output to `student-work/chapter1/outputs/section3_zero_shot.json`.
