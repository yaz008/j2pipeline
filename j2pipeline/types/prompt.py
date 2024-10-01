from dataclasses import dataclass, field
from j2pipeline.template import assemble
from j2pipeline.tcp import client
from typing import Callable, NoReturn

@dataclass(slots=True)
class Prompt:
    path: str
    __callback: Callable[[str], NoReturn] = field(init=False)
    __response: str | None = field(default=None, init=False)

    def __post_init__(self) -> None:
        def callback(response: str) -> NoReturn:
            self.__response = response
            exit(code=0)
        self.__callback = callback

    def ask(self, subs: dict[str, str]) -> str:
        self.__response = None
        prompt: str = assemble(path=self.path, subs=subs)
        with client(on_receive=self.__callback) as clt:
            clt.send(prompt)
        while True:
            if self.__response is not None:
                return self.__response