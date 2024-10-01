from dataclasses import dataclass, field
from os import listdir
from j2pipeline.types.prompt import Prompt
from typing import Self

@dataclass(slots=True)
class Pipeline:
    base_path: str
    __prompts: list[str] = field(init=False)
    __current: int = field(default=0, init=False)

    def __post_init__(self) -> None:
        self.__prompts = [f'{self.base_path}\\{filename}'
                          for filename
                          in listdir(path=self.base_path)]

    def __iter__(self) -> Self:
        return self
    
    def __next__(self) -> Prompt:
        if self.__current == len(self.__prompts):
            raise StopIteration
        prompt: Prompt = Prompt(path=self.__prompts[self.__current])
        self.__current += 1
        return prompt