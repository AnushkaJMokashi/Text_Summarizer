import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"
REPO_NAME="Text_Summarizer"
AUTHOR_NAME="AnushkaJMokashi"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL="anushkamokashi@gmail.com"

setuptools.setup(
    name=SRC_REPO, 
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer with NLP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)