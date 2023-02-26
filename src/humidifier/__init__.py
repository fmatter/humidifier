"""Top-level package for humidifier."""
import logging
import colorlog
from slugify import slugify


handler = colorlog.StreamHandler(None)
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(levelname)-7s%(reset)s %(message)s")
)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.propagate = True
log.addHandler(handler)

__author__ = "Florian Matter"
__email__ = "fmatter@mailbox.org"
__version__ = "0.0.2"


class Humidifier:
    def __init__(self, id_list=None):
        if id_list:
            if isinstance(id_list, list):
                id_list = {"default": id_list}
            self.humids = id_list
        else:
            self.humids = {}
        self.humdict = {}

    def humidify(self, text, key="default", unique=False, **kwargs):
        self.humids.setdefault(key, [])
        self.humdict.setdefault(key, {})
        if not unique and text in self.humdict[key]:
            return self.humdict[key][text]
        first_drop = slugify(text, **kwargs) or "null"
        if first_drop not in self.humids[key]:
            self.humids[key].append(first_drop)
            self.humdict[key][text] = first_drop
            return first_drop
        i = 1
        candidate = f"{first_drop}-{i}"
        while candidate in self.humids[key]:
            i += 1
            candidate = f"{first_drop}-{i}"
        self.humids[key].append(candidate)
        self.humdict[key][text] = candidate
        return candidate

    def get_values(self, key):
        return self.humdict.get(key, None)


og_humidifier = Humidifier()


def humidify(text, key="default", unique=False):
    return og_humidifier.humidify(text, key, unique)


def get_values(key):
    return og_humidifier.get_values(key)
