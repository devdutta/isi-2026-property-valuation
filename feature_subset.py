"""
feature_subset.py  -  the starter feature lists for Module 2 (M2).

Copy these three lists into your notebook. They name the exact columns you
select from AmesHousing.csv. The names have spaces + capitals on purpose -
that is how they appear in the real file, so copy them exactly.

In Colab, paste the three list definitions into your M2 cell, then inspect
them in a notebook cell (a plain `FEATURES` on its own line shows the list).
"""

# 13 numeric features (numbers the model can use directly, after scaling)
NUMERIC = [
    "Overall Qual",  # 1-10 quality rating  - the strongest price driver
    "Gr Liv Area",  # above-ground living area (sq ft)
    "Total Bsmt SF",  # basement area (sq ft)
    "Garage Cars",  # garage capacity (cars)
    "Garage Area",  # garage size (sq ft)
    "Year Built",  # original build year
    "Year Remod/Add",  # last remodel year (= Year Built if never remodelled)
    "Full Bath",  # full bathrooms above ground
    "TotRms AbvGrd",  # total rooms above ground (excludes bathrooms)
    "1st Flr SF",  # first-floor area (sq ft)
    "Lot Area",  # lot / land size (sq ft)
    "Fireplaces",  # number of fireplaces
    "Bedroom AbvGr",  # bedrooms above ground (excludes basement)
]

# 1 categorical (text) feature - one-hot encoded in M4
CATEGORICAL = ["Neighborhood"]

# what we predict (the target). NEVER put this in the features.
TARGET = "SalePrice"

# the full input list = numeric + categorical
FEATURES = NUMERIC + CATEGORICAL


def describe() -> str:
    """Return a human-readable summary of the feature subset.

    Returns:
        str - a multi-line summary. In a notebook, display it with the
        notebook's own output (call describe() on its own line, or pass it
        to the notebook print).

    Example:
        summary = describe()   # then show `summary` in a notebook cell
    """
    lines = [
        f"{len(NUMERIC)} numeric + {len(CATEGORICAL)} categorical "
        f"= {len(FEATURES)} input features; target = {TARGET}",
        "numeric:     " + ", ".join(NUMERIC),
        "categorical: " + ", ".join(CATEGORICAL),
    ]
    return "\n".join(lines)
