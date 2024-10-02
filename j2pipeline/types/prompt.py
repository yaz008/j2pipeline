from dataclasses import dataclass, field
from j2pipeline.template import load_template, render
from j2pipeline.tcp import client
from typing import Callable

@dataclass(slots=True)
class Prompt[T]:
    path: str
    process: Callable[[str], T] = field(default=lambda response: response)
    auto_upper: bool = field(default=True)

    def __call__(self, **subs: str) -> T:
        if self.auto_upper:
            subs = { key.upper(): value for key, value in subs.items() }
        template: str = load_template(path=self.path)
        prompt: str = render(template=template, subs=subs)
        with client() as clt:
            result: str = clt.send(prompt)
        return self.process(result)