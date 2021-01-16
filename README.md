# :hatching_chick: pkm-avian9 :hatching_chick:

Generates a simple mobile-friendly album using Bootstrap. Very useful to bypass the carousell personal account 30-post limit.

## :firecracker: Usage

Specify how you name your images in `config.py`. Feel free to redefine the config dictionary, as long as it remains an iterable. You only need to ensure that the methods `get_images` and `get_name` are defined for each element of the iterable. Then, the generator would still remain compatible.

When done, run `python3 generate_site.py` to generate the required `index.html`. If using Netlify to deploy, you can set the python command as the build command.
