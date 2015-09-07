"""Agent-based model simulation of contra dance partner selection."""


import enum

import mesa


class Role(enum.Enum):
    gent = -1
    lady = 1

    def __invert__(self):
        """Return the opposite role.

        >>> print(~Role.gent)
        Role.lady
        >>> print(~Role.lady)
        Role.gent
        """
        return Role(-self.value)

GENT = Role.gent
LADY = Role.lady


class Dancer(mesa.Agent):
    pass


class PartneringModel(mesa.Model):
    pass
