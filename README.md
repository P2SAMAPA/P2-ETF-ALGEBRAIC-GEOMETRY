# Algebraic Geometry Engine for ETFs

Applies projective geometry (cross‑ratio invariants) to ETF returns. The per‑ETF score measures how projectively unusual an ETF’s last‑day return is relative to the median, min, and max of the universe.

## Features
- Three ETF universes (FI/Commodities, Equity Sectors, Combined)
- Seven rolling windows (63–4536 days)
- Cross‑ratio = (z1,z2;z3,z4) = (z1−z3)(z2−z4)/((z1−z4)(z2−z3))
- References: median, min, max of last‑day returns
- Score = |log(cross‑ratio)|
- Best window automatically selected (largest raw score)
- Two‑tab Streamlit dashboard (auto best + manual window selection)
- Results stored on Hugging Face: `P2SAMAPA/p2-etf-algebraic-geometry-results`

## Usage

1. Set `HF_TOKEN` environment variable.
2. Run training: `python train.py`
3. Launch dashboard: `streamlit run streamlit_app.py`
4. GitHub Actions runs daily.

## Interpretation

- The cross‑ratio is the fundamental invariant of Möbius transformations (projective maps).
- A high cross‑ratio indicates that the ETF’s return is projectively “exceptional” – it cannot be mapped to the reference points by a simple linear fractional transformation.
- This is a novel signal derived from pure algebraic geometry, distinct from graph‑Laplacian methods.

## Requirements

See `requirements.txt`.
