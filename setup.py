from setuptools import find_packages,setuptools

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''

    HYPHEN_E_DOT='-e .'
    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements        


setup(
name = "mlproject",
version="0.0.1",
author="rupanshi",
email="bhadouriarupanshi1995@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')


)