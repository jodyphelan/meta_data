import setuptools


setuptools.setup(

	name="meta-data",
	version="0.1",
	packages=["metadata",],
	license="GPL3",
	long_description="Tools for processing meta data",
	scripts=[
		'scripts/metadata_create_table.py',
		'scripts/metadata_summary.py',
	]
)
