from sys import version
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "chest_cancer_detection"
AUTHOR_NAME = "nihal-das-cv"
SRC_REPO = "ChestCancerDetection"
AUTHOR_EMAIL = "nihaldasofficial@gmail.com"

setuptools.setup(
    name = AUTHOR_NAME,
    version = __version__,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    description = "",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir = { "": "src" },
    packages = setuptools.find_packages(where="src")
)