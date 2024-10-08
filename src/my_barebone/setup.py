import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'my_barebone'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rashik',
    maintainer_email='rashikshrestha01@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_talker = my_barebone.simple_talker:main',
            'simple_listener = my_barebone.simple_listener:main',
            'two_talk_one_listen = my_barebone.two_talk_one_listen:main',
            'one_talk_two_listen = my_barebone.one_talk_two_listen:main',
            'understand_callback_groups = my_barebone.understand_callback_groups:main'
        ],
    },
)
