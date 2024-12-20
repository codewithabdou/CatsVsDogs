import setuptools

with open("README.md", "r" , encoding="utf-8") as fh:
    long_description = fh.read()
    
__version__ = "0.0.0"

REPO_NAME = "Cats-VS-Dogs"
AUTHOR_USER_NAME = "codewithabdou"
SRC_REPO = "Cats-VS-Dogs"
AUTHOR_EMAIL = "kk_habouche@esi.dz"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A CNN classifier for cats vs. dogs, designed as a DL project for learning purposes to understand how the end-to-end process of such projects is conducted.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
    