from setuptools import setup, find_packages

REQUIREMENT_FILE_NAME = "requirements.txt"
REMOVE_PACKAGE = "-e ."


def get_requirement_list(requirement_file_name=REQUIREMENT_FILE_NAME) -> list:
    try:
        requirement_list = None
        with open(requirement_file_name) as requirement_file:
            requirement_list = [requirement.replace("\n", "") for requirement in requirement_file]
            requirement_list.remove(REMOVE_PACKAGE)
        return requirement_list
    except Exception as e:
        raise e


setup(
    name="Housing price prediction",
    license="MIT",
    version="0.0.0",
    description="Project has been completed.",
    author="Avnish Yadav",
    packages=find_packages(),
    install_requires=get_requirement_list()
)


git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin <yours repo link>
git push -u origin main
git push -f origin main
