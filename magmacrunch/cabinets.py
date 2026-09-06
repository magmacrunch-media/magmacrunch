"""The cabinets this arcade ships with, for the screens that have none to show.

Nowhere else. **This is not how the menu is built** — that comes from
enumerating the ``magmacrunch.games`` entry point group, and a hardcoded list
would defeat the whole arrangement. See :mod:`magmacrunch.engine.arcade`.

It exists for the one screen that cannot enumerate anything: an arcade with no
cabinets installed, which has to name something concrete or the player is told
only that the floor is empty. Two surfaces show that — the floor itself and
``magmacrunch --list`` — and they were drifting apart, each naming two of the
three. One tuple, so the next cabinet is one edit, which is what adding the
fourth turned out to cost.

These are PyPI distribution names, which are not the entry point names the menu
sorts by and not the commands a player types. `magmacrunch-thld` installs the
`lava-dome` command and registers the `thld` entry point; `magmacrunch-jhc`
installs `jovian` and registers `jovian`. All three names are correct for a
given cabinet and none of them substitutes for another.
"""

from __future__ import annotations

#: What ``pip install`` takes, in the order the empty floor lists them.
PACKAGES = (
    "magmacrunch-george-boole",
    "magmacrunch-thld",
    "magmacrunch-moonlight-drift",
    "magmacrunch-jhc",
)

__all__ = ["PACKAGES"]
