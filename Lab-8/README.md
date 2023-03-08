**Bhumika Purohit - GEOG 676: GIS Programming - GitHub ePortfolio**



**Introducing the Industry Problem:**



Since the 1800's, the number of wells, oil and gas wells, have exponentially increased throughout the country. As the country has gone through great change and rapid industrialization, there are so many companies with substantial amounts of data. With this is mind, a Master Well Database is the solution to organizing, centralizing, updating, and distributing data. A software tool can be built by utilizing ArcPy and Visual Studio Code to build this Master Well Database. As there are many companies, some of the databases that have their well locations include CAD, ArcGIS, Decision Space Geographics, Petrel, OpenWells, COMPASS, Drilling Info, HSI, and State Regulatory. The designing of the software tool is outlined below with examples of python codes of the most commonly used GIS tasks while creating a software tool like this.






**Creation of the Software Tool Outline:**



1. Choosing Location for Software Development.



As stated earlier, the software tool will be built by utilizing ArcPy and Visual Studio Code. The structure and development of the codes within ArcPy and Visual Studio Code will be located in a GitHub repository. This GitHub repository is used to organize the project of creating the structure and development of the software tool. An example of a GitHub repository and it's structure: https://github.com/bhumika-purohit/purohit-geog676/






2. Loading Several Data Sets that Represents Well Locations.



Loading several data sets, first, requires the need to read the files. This can be done through the use of code. The code can be written to read the data, parse through the data to ultimatily compile and organize the data. In the case of our industry problem of creating a Master Well Database, data sets need to be obtained from databases, including CAD, ArcGIS, Decision Space Geographics, Petrel, OpenWells, COMPASS, Drilling Info, HSI, and State Regulatory. Once these data sets have been read by the software tool, the tool can further the process the creation of the Master Well Database. An example of code that read data to find the areas of various shapes: https://github.com/bhumika-purohit/purohit-geog676/tree/main/Lab-3






3. Determining the Accuracy of the different Well Locations by Inversing Coordinates.



To determine whether the data coordinates of the Well locations are accurate, the consistency of the well data should be examined. An example of this type of code can be found here: https://github.com/bhumika-purohit/purohit-geog676/tree/main/Lab-2






4. Writing to Master Well Geodatabase.



Once the accuracy of the data has been established, the data needs to be written into a master well geodatabase. A tool will be written to build a geodatabase to utilzie further in the process of the creation of the Master Well Database. An example of creating a tool to create a geodatabase: https://github.com/bhumika-purohit/purohit-geog676/tree/main/Lab-4






5. Building a buffer to determine if the Well(s) were put in NAD83 vs. NAD 27.



Typically, buffers are utilized to create areas that can be further analyzed using various tools. In this case, building buffers can help with checking whether the well data points were exported in NAD83 or NAD27. An example of creating buffers: https://github.com/bhumika-purohit/purohit-geog676/tree/main/Lab-5






6. Establishing Confidence of Master Well location.



To establish confidence of master well location, a graduated color Wells map can be built. Using graduated colors map can help with the size of wells and their locations. The map assists with organization to allow for better visualization. An example of building a graduated color Wells: https://github.com/bhumika-purohit/purohit-geog676/tree/main/Lab-6






7. Utilizing aerial images to check Master Well Database.



To support the outcome of the Master Well Database, the success and accuracy of the process needs to be examined. Utilizing aerial images is a way to do so. Utilizing aerial images allows one to examine the spacial aspects of the wells, which can check whether the Master Well Database is successfully and accurately created. An example of using aerial images to check Master Well Database: https://github.com/bhumika-purohit/purohit-geog676/tree/main/Lab-7





**Project Planning Discussion:**



1. Justify the Return on Investment (ROI)



2. Interface with Users



3. Gather requirements



4. Softwares, DBs, etc will be used



5. Code with usages of NumPy, SciPy, PySAL, Model Builder and/or ArcPy



6. Approach commenting, testing, status updates, and reporting



7. Deploy, maintain, and archive your software


