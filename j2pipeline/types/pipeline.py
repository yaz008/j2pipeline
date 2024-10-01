from dataclasses import dataclass, field
from os import listdir
from j2pipeline.types.prompt import Prompt
from typing import Callable

@dataclass(slots=True)
class Pipeline[T]:
    base_path: str
    process: dict[str, Callable[[str], str]] = field(default_factory=dict)
    final_process: Callable[[str], T] = field(default=lambda result: result)

    def __post_init__(self) -> None:
        if '*' not in self.process.keys():
            self.process.update({ '*': lambda response: response })
    
    def __call__(self, prompt: str) -> T:
        result: str = prompt
        for filename in listdir(path=self.base_path):
            name: str = filename[:-len('.j2')]
            prompt: Prompt = Prompt(path=f'{self.base_path}\\{filename}',
                                    process=self.process.get(name, self.process['*']))
            result: str = prompt(PROMPT=result)
        return self.final_process(result)