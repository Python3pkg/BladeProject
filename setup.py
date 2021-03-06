from setuptools import setup, find_packages

setup(
    name='Blade',
    version='0.1',
    description='A simple pygame demo.',
    long_description='A small demo of a fencing-inspired RPG combat system. Contains tutorial and a final boss fight. Badly-written RPG dialog and blatant Undertale/Pokemon Mystery Dungeon references are complementary.',
    url="This project doesn't have one at the moment.",
    author="AardvarkTotoro",
    keywords='game demo pygame fencing',
    packages=find_packages(),
    install_requires=['pygame'],
    package_data={'Blade':['BladeCursor.png','BladeBlade.png','BladeField.png','FakeScreen.png','MoonScreen.png','RangeLines.png','StartLines.png','EdithBlade.png','Shout.ogg','ForkClick.ogg','EdithScreen.png','EdithBossIntro.png','Virtual_Counterpoint_2.ogg','Your_Best_Friend_[First_Draft_.ogg','Hit.ogg','FireBase.png','Fireball.png','Clap.ogg','Whoosh.ogg','Shoop.ogg']}
    )
    
