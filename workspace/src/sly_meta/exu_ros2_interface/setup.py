from setuptools import setup

package_name = 'exu_ros2_interface'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vscode',
    maintainer_email='msereinig@gmx.net',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'exu_test = exu_ros2_interface.exu_test:main',
            'simple_pub_sub = exu_ros2_interface.simple_pub_sub:main'
        ],
    },
)
