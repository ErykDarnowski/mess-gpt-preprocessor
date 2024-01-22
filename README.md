# mess-gpt-preprocessor

FB Messenger transcription preprocessor to create data for fine-tuning ChatGPT.

## Usage

1. Run the `scroll.js` and `download.js` scripts to get the `transcript.txt` input file. (**these are private for now, so don't look for them on my GH**)
2. Change the config in `./__main__.py`.
3. Run script: `py ./__main__.py`
4. Upload `output.jsonl` to the OpenAI Fine-tuning API.
