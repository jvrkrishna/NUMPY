############### why we require anaconda ###########
'''
Anaconda is a popular open-source distribution that provides a robust environment for data science, machine learning, and scientific computing.
'''

############ Steps to install anaconda #############
'''
1. Download Anaconda Installer:
Go to the official Anaconda website:
https://www.anaconda.com/products/individual

Click on "Download" and select the appropriate installer for your operating system (Windows, macOS, or Linux). 
Choose the version based on your Python preference (usually the latest version is fine).

Installing Anaconda is straightforward, and here are the steps to do it on different operating systems:

2. Install Anaconda (Windows):
Run the Installer:

After the download is complete, double-click the .exe file to launch the installer.
Follow the Installation Wizard:

Select "Add Anaconda to my PATH environment variable" (optional but recommended) to make it easier to use Anaconda from the command line.
Choose "Install for Just Me" unless you want to install for all users.
Choose the default options for the installation location, unless you need to change it.
Complete Installation:

Click "Install", and the installation process will begin. Once done, click "Next" and then "Finish".

3. Verify Installation:
Once Anaconda is installed, open a terminal or command prompt and type:
bash

conda --version
If you see something like conda 23.1.0 (or a similar version), then the installation was successful.

4. Launch Anaconda Navigator (Optional)
Anaconda also comes with a GUI tool called Anaconda Navigator, which provides a graphical interface to manage environments and packages:

On Windows/macOS, you can search for "Anaconda Navigator" in your start menu or applications folder to launch it.
On Linux, you can type anaconda-navigator in the terminal to open it.

5. Create a New Environment (Optional)
It’s a good practice to create isolated environments for different projects. You can do this with Conda in the terminal:
bash
conda create --name myenv python=3.9
conda activate myenv
This will create a new environment named myenv with Python 3.9 and activate it.
'''

'''
Open Anaconda Navigator ---------- Launch Jupyter Notebook ----- It will Open Chrome Browser in that click on New ----- select Python
Ctrl+Enter ------ To run the code
Alt+Enter ------- To insert to new cell

If we want to install Numpy in cmd prompt:
--> pip install numpy

In Anaconda 
--> !pip install numpy

Create sample program
import numpy as np
arr=np.arange(100)
print(arr)

Running Anaconda Navigator is not good it is basically from C drive so we use Anaconda Prompt to and Execute jupyter notebook.
'''