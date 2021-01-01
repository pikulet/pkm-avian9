# pkm-avian9

Generates a simple bootstrap-based site for an album library. Very useful to bypass the carousell personal account 30-post limit.

1. Specify how you name your images in `config.py`. Feel free to redefine the config dictionary, as long as it remains an iterable. The generator calls `get_images` and `get_name` for each element of the iterable.

2. `python3 generate_site.py` to generate the required `index.html`

3. Create a free netlify account and deploy
