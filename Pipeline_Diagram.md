# Project Pipeline Diagram

Two files in this folder:

| File | Use |
|------|-----|
| **`Project_Pipeline.png`** | **Ready-to-use image** — drop straight into a slide or screen-share in Teams. Rendered 22 Jun 2026 from the HTML below. |
| **`Project_Pipeline.html`** | **Editable source (canonical)** — open in a browser, edit boxes/text, then re-screenshot the `.canvas` element to refresh the PNG. On-brand with the Handbook + Build Spec. |

> The **PNG is the reliable image**; the **`.html` is the reliable editable source**.

## What it shows (top → bottom)
1. **Load housing data** (pandas · `AmesHousing.csv` → `df_raw`, 2930×82)
2. → **Clean & pick 14 features** (drop 5 outliers · choose the subset → `X`, `y`)
3. → **Explore the data (EDA)** (price distribution · what correlates with price)
4. → **Split + preprocess** (train/test seed 42 · impute · scale · one-hot → `preprocessor`)
5. → branches into the **two models**: Linear Regression (baseline, R² ≈ 0.88) and Random Forest (R² ≈ 0.92)
6. → both feed **Evaluate, compare & select the final model** (RMSE · MAE · R² · feature importance · charts) — the winner is Random Forest
7. → **Predict prices** with the chosen model — a single house you type in, or a whole batch at once (**the app / payoff**)
8. → **AI assistant** (Groq, free) — explains each price + describe-a-house → price + an **optional UI** (ipywidgets, dashed)

The two models + evaluation + the prediction app are highlighted as the **data-science core — the graded part**. The **honesty rule** is called out at the bottom: the model predicts, the LLM only explains. Everything runs in one Jupyter notebook on Google Colab. Maps to Modules M1–M10 in the Build Specification (M0 = setup).
