# humidifier

Create human-friendly IDs from strings.

![License](https://img.shields.io/github/license/fmatter/humidifier)
[![Tests](https://img.shields.io/github/actions/workflow/status/fmatter/humidifier/tests.yml?branch=main&label=tests)](https://github.com/fmatter/humidifier/actions/workflows/tests.yml)
[![Linting](https://img.shields.io/github/actions/workflow/status/fmatter/humidifier/lint.yml?branch=main&label=linting)](https://github.com/fmatter/humidifier/actions/workflows/lint.yml)
[![Codecov](https://img.shields.io/codecov/c/github/fmatter/humidifier)](https://app.codecov.io/gh/fmatter/humidifier/)
[![PyPI](https://img.shields.io/pypi/v/humidifier.svg)](https://pypi.org/project/humidifier)
![Versions](https://img.shields.io/pypi/pyversions/humidifier)

The typical use case for `humidifier` is that you have some string (a word, a name, a phrase...) that you want to turn into a human-friendly ID.
For example, your project has URLs containing IDs, and it would be nicer to have `/record/an-example` instead of `/record/21937218`.
Such IDs are easy to remember and can function as a preview for the database entry.
This can be achieved with the excellent [`python-slugify`](https://github.com/un33k/python-slugify), to which humidifier adds the option to generate unique IDs


## Usage
Using `humidifier` is rather simple:

```python
from humidifier import humidify

id_1 = humidify("dog", unique=True)  # 'dog'
id_2 = humidify("dog", unique=True)  # 'dog-1'
id_3 = humidify("dög", unique=True)  # 'dog-2'
id_4 = humidify("ʔɚ", unique=True)  # 'null'
id_5 = humidify("ʔɚ", unique=True)  # 'null-1'
```

If your strings come from different populations that you would like to keep distinct in the generated IDs, there is an optional `key` argument:

```python
from humidifier import humidify

id_1 = humidify("dog", key="animals", unique=True)  # 'dog'
id_2 = humidify("dog", key="quadripeds", unique=True)  # 'dog'
id_3 = humidify("dög", key="animals", unique=True)  # 'dog-1'
id_4 = humidify("dög", key="animals", unique=True)  # 'dog-2'
```

If you are working with an existing set of IDs:

```python
from humidifier import Humidifier
hum = Humidifier(["dog"])
hum.humidify("dog", unique=True)  # 'dog-1'
```

If you only want to generate a new ID for each distinct string:

```python
from humidifier import humidify

humidify("dög")  # 'dog'
humidify("dög")  # 'dog'
humidify("dog")  # 'dog-1'
```

You can also use any of the arguments described for [`python-slugify`](https://github.com/un33k/python-slugify).
The arguments `max_length` for truncating, `separator` for something other than `-` in between parts, and `replacements` may be of particular interest when generating IDs.