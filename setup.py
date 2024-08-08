from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Edit below variables as per your requirements -
REPO_NAME = "Movie-Recommender-System-Using-Machine-Learning"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name="MovieRecommenderSystem",  # A more descriptive package name
    version="0.0.1",
    author="Tharun Kumar",  # Updated author name
    description="A small package for Movie Recommender System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    author_email="entbappy73@gmail.com",
    packages=find_packages(where=SRC_REPO),  # Automatically find all packages in the src directory
    package_dir={'': SRC_REPO},  # Specify the src directory as the root
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)