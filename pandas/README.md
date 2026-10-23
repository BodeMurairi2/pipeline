# Pandas

Introduction to `pandas` for data pipelines.

## Tasks

| File | Description |
| ---- | ----------- |
| `0-from_numpy.py` | `from_numpy(array)` creates a `pd.DataFrame` from a `np.ndarray`, with columns labeled `A`, `B`, `C`, ... in alphabetical order |
| `1-from_dictionary.py` | Creates a `pd.DataFrame` `df` from a dictionary, with columns `First` and `Second` and rows labeled `A`–`D` |
| `2-from_file.py` | `from_file(filename, delimiter)` loads data from a file as a `pd.DataFrame` |
| `3-rename.py` | Renames `Timestamp` to `Datetime`, converts it to datetime values and displays only `Datetime` and `Close` |
| `4-array.py` | Converts the last 10 rows of the `High` and `Close` columns into a `numpy.ndarray` |
| `5-slice.py` | Slices the `High`, `Low`, `Close` and `Volume_(BTC)` columns, taking every 60th row |
| `6-flip_switch.py` | Transposes the rows and columns and sorts the data in reverse chronological order |
| `7-high.py` | Sorts the `pd.DataFrame` by the `High` price in descending order |
| `8-prune.py` | Removes the entries where `Close` is `NaN` |
| `9-fill.py` | Removes `Weighted_Price` and fills in the missing data points |
| `10-index.py` | Indexes the `pd.DataFrame` on the `Timestamp` column |
| `11-concat.py` | Concatenates the start of the bitstamp table onto the top of the coinbase table, with keys |
| `12-hierarchy.py` | Concatenates both tables from `1417411980` to `1417417980` with `Timestamp` as the first index level, in chronological order |
| `13-analyze.py` | Calculates descriptive statistics for all columns except `Timestamp` |
| `14-visualize.py` | Cleans the data and plots it from 2017 onwards at daily intervals |
