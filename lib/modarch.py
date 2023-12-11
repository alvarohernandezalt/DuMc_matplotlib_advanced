import itertools

debug = False
unknown_group = "unknown"
top_level_group = "matplotlib"

matplotlib_groupings = {
    "axes": ["matplotlib.axes"],
    "backend_bases": ["matplotlib.backend_bases"],
    "backends": ["matplotlib.backends"],
    "cbook": ["matplotlib.cbook"],
    "core": ["matplotlib"],
    "misc": ["matplotlib._cm",
             "matplotlib._cntr",
             "matplotlib._color_data",
             "matplotlib._image",
             "matplotlib._layoutbox",
             "matplotlib._mathtext_data",
             "matplotlib._pylab_helpers",
             "matplotlib._tri",
             "matplotlib._version",
             "matplotlib.afm",
             "matplotlib.artist",
             "matplotlib.axis",
             "matplotlib.blocking_input",
             "matplotlib.category",
             "matplotlib.cm",
             "matplotlib.collections",
             "matplotlib.color",
             "matplotlib.compat",
             "matplotlib.dates",
             "matplotlib.delaunay",
             "matplotlib.docstring",
             "matplotlib.finance",
             "matplotlib.font",
             "matplotlib.sphinxext",
             "mpl_tool"]}

reverse_matplotlib_groupings = dict(list(
    itertools.chain(*[[(x, group) for x in mod_part]
                      for (group, mod_part) in matplotlib_groupings.items()])))

def get_group(mod_name):
    if not isinstance(mod_name, str):
        raise TypeError('mod_name must be a string')

    mod_name = mod_name.strip()
    if mod_name == "__main__":
        return mod_name
    if mod_name == "matplotlib":
        return top_level_group
    if mod_name in reverse_matplotlib_groupings:
        if debug:
            print("[X] Found quick match for '{}'!".format(mod_name))
        return reverse_matplotlib_groupings[mod_name]
    for (mod_part, group) in reverse_matplotlib_groupings.items():
        if mod_name.startswith(mod_part):
            if debug:
                print("[-] Found slow match for '{}'...".format(mod_name))
            return group
    if debug:
        print("[ ] Couldn't find match for '{}' ...".format(mod_name))
    return unknown_group

__all__ = ["matplotlib_groupings", "reverse_matplotlib_groupings", "get_group"]