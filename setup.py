from setuptools import setup

setup(
    name='instasend',
    version='0.1.0',
    author='Tomas Santana',
    description="A Simple library to send messages to Instagram DMs. Wrapper for the Instagram API with Instagram Login.",
    url='https://github.com/tomas-santana/instasend',
    author_email="tomas@cervant.chat",
    license='MIT',
    packages=['instasend'],
    install_requires=[
        'requests',
        'pydantic>=2.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
