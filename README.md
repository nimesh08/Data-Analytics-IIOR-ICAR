# Oilseed Atlas

A responsive oilseeds statistical information dashboard for exploring crop production, imports, exports, and year-over-year changes.

**[Open the dashboard](https://nimesh08.github.io/Data-Analytics-IIOR-ICAR/)**

## Data and provenance

This portfolio dashboard is not affiliated with or endorsed by ICAR or IIOR. All values are synthetic, deterministically generated example data for 2019–2024. The years identify sample observations, not software creation dates. Do not use this dataset for research, policy, or agricultural decisions.

## Features

- Production, import, export, and net trade indicators
- Crop and year filters with synchronized charts and tables
- Annual trends and crop production shares
- Searchable crop table and CSV export of the current table selection
- Responsive desktop and mobile interface
- No frontend build step or charting dependencies

## Run locally

Use Python's built-in static server:

```sh
python -m http.server 8000
```

Then open http://localhost:8000. Alternatively, use the included Flask server:

```sh
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. GitHub Pages serves the static interface; Flask is an optional local server and is not executed by GitHub Pages.

## Implementation

Semantic HTML, responsive CSS, vanilla JavaScript, SVG charts, and optional Python/Flask serving. Data is generated in `app.js` using a fixed seed. Volumes are in million tonnes. Trade balance equals exports minus imports. Year-over-year production change compares the same selected crops to the previous year; 2019 has no preceding observation.

## Author

Nimesh Cheedella

