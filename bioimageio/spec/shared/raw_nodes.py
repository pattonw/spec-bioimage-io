"""shared raw nodes that shared transformer act on"""

from dataclasses import dataclass
from pathlib import Path
from typing import List

from marshmallow import missing


@dataclass
class Node:
    pass


@dataclass
class URI(Node):
    """URI as  scheme:[//authority]path[?query][#fragment]"""

    scheme: str = missing
    authority: str = missing
    path: str = missing
    query: str = missing
    fragment: str = missing

    def __str__(self):
        """scheme:[//authority]path[?query][#fragment]"""
        return (
            (self.scheme + ":" if self.scheme else "")
            + ("//" + self.authority if self.authority else "")
            + self.path
            + ("?" + self.query if self.query else "")
            + ("#" + self.fragment if self.fragment else "")
        )


@dataclass
class ImportablePath(Node):
    filepath: Path = missing
    callable_name: str = missing


@dataclass
class ImportableModule(Node):
    module_name: str = missing
    callable_name: str = missing


@dataclass
class ImplicitInputShape(Node):
    min: List[float] = missing
    step: List[float] = missing

    def __len__(self):
        return len(self.min)


@dataclass
class ImplicitOutputShape(Node):
    reference_input: str = missing
    scale: List[float] = missing
    offset: List[int] = missing

    def __len__(self):
        return len(self.scale)