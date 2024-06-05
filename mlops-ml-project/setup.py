import setuptools

with open("README.md", 'r', encoding="utf-8") as f:
    long_rescription = f.read()


__version__ = '0.0.0'

REPO_NAME = "end-to-end-ML-project-with-dvc-mlflow"
AUTHOR_USER_NAME = "test"
SRC_REPO = "mlops-ml-project"
AUTHOR_EMAIL = "test@test.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="description for the project",
    long_description=long_rescription,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"", "src"},
    packages=setuptools.find_packages(where="src")
)