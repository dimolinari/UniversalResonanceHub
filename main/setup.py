from setuptools import setup, find_packages

setup(
    name="UniversalResonanceHub",
    version="0.1.0",
    author="Dicaoz – Eduardo Molina 🇪🇨",
    description="Sistema de Resonancia Universal: generación simbólica fractal con codificación cuántico-lingüística",
    packages=find_packages(include=["main", "main.*"]),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "scikit-learn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
