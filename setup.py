from setuptools import setup
from importlib.metadata import entry_points

setup(
    name="DnD_Roller",
    version="1.0.0",
    author="Karsten Courtney",
    author_email="ftwkrc@gmail.com",
    packages=["dnd_roller"],
    entry_points={
        "console_scripts": [
            "dnd_roll=dnd_roller.__main__:main"
        ]
    },
    requires=[
        "colorama"
    ]
)