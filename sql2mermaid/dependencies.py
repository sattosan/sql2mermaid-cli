from dataclasses import dataclass
from typing import Iterator, List


@dataclass
class Dependency:
    start: str
    mark: str
    end: str


class Dependencies:
    def __init__(self) -> None:
        self.values: List[Dependency] = []

    def __call__(self) -> List[Dependency]:
        return self.values

    def __iter__(self) -> Iterator[Dependency]:
        yield from self.values

    def add(self, x: Dependency, /) -> None:
        if x not in self:
            self.values.append(x)
