from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="memeclip",
    version="0.1.0",
    author="MemeClip",
    author_email="service.memeclip@gmail.com",
    description="Official Python SDK for MemeClip's AI Meme Generator API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/memeclip/memeclip-ai-api",
    project_urls={
        "Bug Tracker": "https://github.com/memeclip/memeclip-ai-api/issues",
        "Documentation": "https://memeclip.ai",
        "Homepage": "https://memeclip.ai",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.25.0",
        "pillow>=8.0.0",
    ],
    keywords="meme, ai meme generator, video meme generator, video meme, meme image",
) 
