from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name = 'test',         # How you named your package folder (test)
    packages = ['test'],   # Chose the same as "name"
    version = '0.0.1',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    author = 'Jonathan McMillan',                   # Type in your name
    author_email = 'jmcmillan@watlow.com',      # Type in your E-Mail
    url = 'https://github.com/watlow-jmcmillan/test-python-package',   # Link to github page for the repo
    #download_url = 'https://github.com/RaaLabs/TSIClient/archive/v_0.7.tar.gz',    # If you create releases through Github, then this is important
    keywords = ['Python package', 'test'],   # Keywords that define your package best
    install_requires=[              # External python dependencies
            'requests',             # Include any packages from pip required
            'pandas'
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
