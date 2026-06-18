# SICSS-TEST



This repository includes a minimal filter for congressional bills:

- Congress range: 107 through 118 (inclusive)
- Match rule: the word `china` must appear in the **bill title**
- Label rule: matching bills are labeled exactly `China`

## Usage

Given a JSON array of bills with at least `congress` and `title` fields:

```bash
python /home/runner/work/SICSS-TEST/SICSS-TEST/china_bills.py /path/to/bills.json
```

The script prints matching bills as CSV with a `label` column set to `China`.
