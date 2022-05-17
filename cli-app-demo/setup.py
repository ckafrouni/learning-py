import setuptools

setuptools.setup(
	name ='qsdf',
	version ='1.0.0',
	entry_points={
		'console_scripts': ['mytool = App.__main__:main']
	}
)