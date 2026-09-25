# Student Work

This folder contains my local work for the Hugging Face LLM course.

The upstream course content stays in `chapters/`. Generated notebooks from the course are kept in `nbs/`, which is ignored by Git. Notebooks and notes that show my progress live here so they can be committed and demonstrated.

## Workflow

Local folder:

```text
C:\Users\ruslan.marchanka\hf-course-local
```

VS Code/Jupyter kernel: `HF Course Local`.

1. Generate upstream notebooks into `nbs/`:

   ```powershell
   .\.venv\Scripts\python.exe utils\generate_notebooks.py --output_dir nbs
   ```

2. Copy the notebook I am actively working on into `student-work/notebooks/`.
3. Run it locally, keep useful outputs, and record observations in the chapter notes.
4. Commit only the learning artifacts from `student-work/` plus any intentional tooling fixes.

Note: `git` is not currently available in PATH on this machine. Install Git for Windows before committing and pushing from the local folder.

## Progress

| Chapter | Section | Status | Artifact |
| --- | --- | --- | --- |
| 1 | 3. Transformers, what can they do? | Sentiment and zero-shot complete | `chapter1/outputs/` |
