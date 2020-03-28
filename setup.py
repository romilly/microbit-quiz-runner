import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="microbit-quiz-runner", # Replace with your own username
    version="0.1.0",
    author="Romilly Cocking",
    author_email="romilly.cocking@gmail.com",
    description="Quiz Game Runner using PC/Pi and microbits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/romilly/microbit-quiz-runner",
    packages=setuptools.find_packages(),
    package_data={
        'quizrunner' : ['tick.png','cross.png']
    },
    install_requires=[
        'guizero', 'pyserial', 'microfs'
    ],
    scripts=['bin/run-game'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)