# Smart Content Command Center

A simple Streamlit dashboard that displays YouTube video metadata from a cached `youtube_data.json` file.

## What it does

- Loads a JSON file exported from an automation pipeline (for example, n8n).
- Detects common response shapes like a top-level list or a `data` object.
- Renders each video with a thumbnail, title, author, publish date, and link.

## Files

- `app.py` - Streamlit app entrypoint.
- `youtube_data.json` - Example JSON cache file used by the app.

## Requirements

- Python 3.8+
- `streamlit`

## Install

```bash
python -m pip install streamlit
```

## Run

```bash
streamlit run app.py
```

Then open the displayed local URL in your browser.

## Data format

The app expects `youtube_data.json` to contain either:

- a list of video objects, or
- a list containing a dict with a `data` key, or
- a dict with a `data` key.

Each video object may include:

- `title`
- `link`
- `thumbnail`
- `author`
- `pubDate`

If the file is missing or cannot be parsed, the app displays a warning or error message.

## Notes

- `DATA_PATH` in `app.py` is currently hard-coded to `/workspaces/codespaces-blank/youtube_data.json`.
- If you move the app or data file, update `DATA_PATH` accordingly.
