import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'rviz_tools_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'meshes'), glob(os.path.join('meshes', '*.*')))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='luis',
    maintainer_email='luis@robtech.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rviz_tools_node = rviz_tools_package.rviz_tools_node',
            'demo = rviz_tools_package.demo',
        ],
    },
)
