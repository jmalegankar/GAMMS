# Getting Started
**Gamms** is a library designed to simulate adversial games in a graph based world. This guide will help you quickly install and set up Gamms so you can start experimenting as soon as possible.

## Python Requierement
Gamms requires **Python 3.9** or later. If you already have a suitable version installed, skip to [Installation and Setup](#installation-and-setup).

Otherwise, visit the official Python download page to install a compatible version for your device (Windows, Mac, or Linux): [Python]: https://www.python.org/downloads/

## Installation and Setup

Before installing **Gamms**, ensure that [pip](https://pypi.org/project/pip/) is installed. Most Python distributions include pip by default; if you need to install it separately, follow the instructions on the pip documentation page.

Once pip is set up, use the appropriate commands below for your operating system.

- On **Windows**:
```sh
python -m pip install gamms
```

   - On **Mac/Linux**:
```sh
python3 -m pip install gamms
```

## Creating a Project Folder and Virtual Environment

1. **Create a new folder** in the directory where you want your project to live. We'll name it `gamms`:

   mkdir gamms
   cd gamms

2. **Create a Python virtual environment** within this folder. You can do this using `python` or `python3`, depending on your system:

   python -m venv venv

   This command will create a subfolder named `venv` that contains your virtual environment files.

3. **Activate the virtual environment**:

   - On **Windows**:
```sh
venv\Scripts\activate
```
   - On **Mac/Linux**:
```sh
source venv/bin/activate
```

4. **Install Gamms** within the virtual environment:
```sh
python -m pip install gamms
```
5. **Verify your installation**:
```py
   import gamms
   print("Gamms version:", gamms.__version__)
```

Once these steps are completed, you will have **Gamms** installed in a clean virtual environment. Remember to activate the virtual environment (step 3) whenever you want to work on your project.


## Installing Git, Wget, and Cloning Examples

### 1. **Ensure Git and Wget are installed** on your system.
   - If you're missing Git or Wget, install them using your package manager or from the official websites:
     - **Windows**:
       - [Git for Windows](https://git-scm.com/download/win)
       - [Wget for Windows](https://eternallybored.org/misc/wget/)
     - **Mac**:
       - [Git via Homebrew](https://brew.sh/)
       - [Wget via Homebrew](https://brew.sh/)
     - **Linux**:
       - `sudo apt-get install git wget` (Debian/Ubuntu)
       - `sudo dnf install git wget` (Fedora)
       - `sudo pacman -S git wget` (Arch)

### 2. **Install Git using pip (if you prefer Python tools)**:
```sh
python -m pip install git
```

### 3. **Install Wget using pip (if you prefer Python tools)**:
```sh
python -m pip install wget
```

### 4. Cloning or Downloading the `examples` Directory

**Clone or download the `examples` directory** from [GAMMSim/gamms](https://github.com/GAMMSim/gamms/tree/main/examples).

#### Option A: Using Git

```sh
git clone https://github.com/GAMMSim/gamms.git
mv gamms/examples examples
```
#### Option B: Using Wget (to download the entire repo as a ZIP)
```sh
wget https://github.com/GAMMSim/gamms/archive/refs/heads/main.zip
unzip main.zip
mv gamms-main/examples examples
rm -rf gamms-main main.zip
```

### 5. Running `create_graph.py`

#### **Execute** the script:
```sh
python create_graph.py
```
Verify that a `.pkl` file is successfully created. This indicates that the graph has been created properly.

### 6. Creating Strategy and Configuration Files

#### Step 1: **Create a folder** named `games` (in the root of your project directory or wherever you prefer):
```sh
mkdir games
```
#### Step 2: **Inside the `games` folder**, create three Python files:
   - **`blue_strategy.py`**  
   - **`red_strategy.py`**  
   - **`config.py`**

#### Step 3: **Implement** the logic for each file according to your specific needs. For example:
   - `blue_strategy.py` might define functions or classes related to the Blue team's strategy.
   - `red_strategy.py` might define functions or classes related to the Red team's strategy.
   - `config.py` might define shared constants, environment variables, or other settings.

