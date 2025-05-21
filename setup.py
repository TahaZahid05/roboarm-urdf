from setuptools import find_packages, setup

package_name = 'my_robot_rviz'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/meshes', [
        'meshes/Base.dae',
        'meshes/Antebrazo.dae',
        'meshes/Basedelagarra.dae',
        'meshes/Brazo.dae',
        'meshes/EjeCentral.dae',
        'meshes/Muteca.dae',
        'meshes/Pinza1.dae',
        'meshes/Pinza2.dae',
        'meshes/Barra1.dae',
        'meshes/Barra2.dae',
        'meshes/Engranaje1.dae',
        'meshes/Engranaje2.dae',
        'meshes/Tapapgarra.dae',
    ]),
        ('share/' + package_name + '/urdf', ['urdf/my_robot.urdf']),
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='taha',
    maintainer_email='taha@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
