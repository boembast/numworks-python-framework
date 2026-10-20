# numworks-python-framework

## DISCLAIMER: This project is currently in development and does not have a version ready for use. It currently holds the files that are tests I have done or am doing to figure out the whereabouts of the framework. Some of the files intended to be libraries may have leftover code to test said libraries. Functionality of any file is not guaranteed.

Framework for python on the Numworks graphing calculator to make GUI's (description subject to change)


# Using the repository yourself
To use this repo, depending on your system you'll want to make a virtual environment. But regardless, you'll need the package list of requirements.txt which is the result of `pip freeze`. This contains all the packages needed to be installed with pip. In VS Code you can also just use the Python extension(s) to create a custom virtualenv, in which you will be able to choose something with dependencies in the choice name, where you can then put in `requirements.txt` to have VSc install the requirements at the setup. You will also need the `python3-tk`, `python3-pip` and `python3-venv` packages to create the virtual environment. These are the debian variants, I do not know what they are on other distributions / windows as of currently. There might be more packages required that I am not aware of at this time, possibly subject to change.

---

To use this repo, you'll want to install [uv](https://docs.astral.sh/uv/). Depending on which operating system you are on, you can use the following command:

**Linux / MacOS**
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```
**Windows (through PowerShell)**
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

If you are uncomfortable with piping scripts into bash (or PowerShell), you can check out other options [here](https://docs.astral.sh/uv/getting-started/installation/).

After this, ==I don't know what to do yet, I'm going to test it out now==