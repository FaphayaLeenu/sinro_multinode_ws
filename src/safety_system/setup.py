from setuptools import find_packages, setup

package_name = 'safety_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='leenu',
    maintainer_email='faphayaleenu@karunya.edu.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
        entry_points={
        'console_scripts': [
            'temp = greenhouse_system.temp_node:main',
            'hum = greenhouse_system.hum_node:main',
            'brain = greenhouse_system.brain_node:main',
            'sprinkler = greenhouse_system.sprinkler_node:main'
        ],
    },
)
