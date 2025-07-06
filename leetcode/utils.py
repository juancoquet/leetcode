from typing import Callable, Iterable, TypeVar

T = TypeVar("T")
U = TypeVar("U")


def group(things: Iterable[T], key: Callable[[T], U]) -> dict[U, list[T]]:
    groups: dict[U, list[T]] = {}
    for thing in things:
        groups.setdefault(key(thing), []).append(thing)
    return groups
