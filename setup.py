from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="auto_screenshot_tool",
    version="0.1.0",
    author="Asmita Timalsena",
    description="Automatically take screenshots at intervals",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    url="https://github.com/AsmitaTimalsena/auto_screenshot_tool",
    install_requires=["pyautogui"],
    python_requires=">=3.6",
)