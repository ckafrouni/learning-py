
import dataclasses
import typing
from urllib import response

@dataclasses.dataclass
class Person:
	firstname: 	str
	lastname:	str
	age:		int
	sex:		typing.Literal['man', 'woman']


def input_firstname() -> str:
	return input('First name > ')

def input_lastname() -> str:
	return input('Last name > ')

def input_age() -> str:
	return input('Age > ')

def input_sex() -> str:
	return input('Sex ([wo]man) >')

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