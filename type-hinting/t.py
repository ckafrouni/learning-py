import dataclasses
import typing

Date = typing.NamedTuple('Date', [('dd', int), ('mm', int), ('yyyy', int)])

@dataclasses.dataclass
class Employee:
	fname: str
	sex: typing.Literal['Man', 'Woman']
	age: int
	birthday: Date
	signature: typing.Callable[[], str]

print(Employee('chris', 'Man', 15, Date(25,11,2000), lambda : 'MySigg'))

x: typing.Sequence[int]

