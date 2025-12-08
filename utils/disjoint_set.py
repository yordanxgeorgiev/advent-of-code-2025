from typing import Generic, Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


class DisjointSet(Generic[T]):
    """A simple disjoint set implementation."""

    def __init__(self):
        self._parents = {}  # direct or indirect parent of each node
        self._sizes = {}  # size of connected component per node
        self._components = 0  # total number of connected components

    @property
    def components_count(self) -> int:
        """Number of connected components."""
        return self._components

    def add(self, x: T) -> None:
        """Adds an element to the set."""
        if x not in self._parents:
            self._parents[x] = x
            self._sizes[x] = 1
            self._components += 1

    def union(self, a: T, b: T) -> None:
        """Union the sets containing `a` and `b`."""
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        # merge smaller tree into bigger one
        if self._sizes[a] < self._sizes[b]:
            b, a = a, b

        self._parents[b] = a
        self._sizes[a] += self._sizes[b]
        self._components -= 1

    def find(self, x: T) -> T:
        """
        Finds the connected set an element is part of. Returns the
        representative element of that set.
        """
        self.add(x)
        if self._parents[x] != x:
            self._parents[x] = self.find(self._parents[x])
        return self._parents[x]

    def get_component_size(self, x: T) -> int:
        """Returns the size of the given connected component."""
        return self._sizes[self.find(x)]

    def get_components(self) -> list[T]:
        """Returns all the connected components in the disjoint set."""
        components = set()
        for x in self._parents:
            components.add(self.find(x))
        return list(components)
