# Project 2 Workflow
### Step 1: Create a new environment "arcpy_clone"
In the Anaconda Prompt:
&nbsp;>conda env list
&nbsp;>conda create -n arcpy_clone --clone "C:\Users\hli69\.conda\envs\arcgispro-py3-clone"
&nbsp;>conda activate arcpy_clone
&nbsp;>python
&nbsp;&nbsp;&nbsp;>>> import arcpy
&nbsp;&nbsp;&nbsp;>>> quit()
### Step 2: install GEE library
In the Anaconda Prompt:
&nbsp;>pip install earthengine-api
&nbsp;>python
&nbsp;&nbsp;&nbsp;>>> import ee
&nbsp;&nbsp;&nbsp;>>> ee.Authenticate()
&nbsp;&nbsp;&nbsp;>>> ee. Initialize()
Go to the https://code.earthengine.google.com/, on the right up corner, Click on the avatar icon, find the Project Info, copy the name of the Cloud Project: ee-hanqi
&nbsp;&nbsp;&nbsp;>>> ee. Initialize(project='ee-hanqi')
### Step 3: Create a work folder for this project
Go into this folder, right click in blank, Open in Terminal
&nbsp;>code . 
This command will open this folder in VSCode.
### Step 4: Create a Notebook for this project
Project2_Hanqi.ipynb
Select the kernel: arcpy_clone
### Step 5: Convert the code from Project2_Hanqi.ipynb to Project2_Hanqi.py
Usage:
python Project2_Hanqi.py "F:\OneDrive - Louisiana State University\LSU_Course\GEOG\GEOG 4057 GIS Programming\GEOG4057_Hanqi\Projects\Project_2_Hanqi" boundary.csv pnt_elev2 32119
### Step 6: Create a ArcGIS Pro script tool using the Project2_Hanqi.py







