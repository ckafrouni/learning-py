
import dataclasses
import typing
from urllib import response

@dataclasses.dataclass
class Person:
	firstname: 	str
	lastname:	str
	age:		int
	sex:		typing.Literal['man', 'woman']

def flow():
	steps: list[callable] = [
		input_firstname,
		input_lastname,
		input_age,
		input_sex
	]

	for s in steps:
		yield s()


def main():
	engine = create_engine("sqlite:///database.db")

	specs = []
	flow_gen = flow()
	for response in flow_gen:
		if response == 'q':
			break
		specs.append(response)
	else:
		print(Person(*specs))


if __name__ == '__main__':
	main()