# Arctic Challenge 2022

This repository is for my contribution to the 2022 Arctic Challenge Hackathon in Skellefteå, Sweden. 22-24 November 2022.

## The task: Data collection framework for collaboration and co-presence in a virtual reality environment.
The challenge is to create a solution, for example, a VR framework, which collects and integrates data from several sources for virtual reality collaboration and co-presence applications with a particular focus on medical
training, and to collect sample data with the framework and make standardized data cleanup for analysis.

### Requirements:
- Microsoft Hololens2
- multiple environmental and physiological sensors
- MongoDB account and database

### Overview:
The user has to create a MongoDB account, create a database, and retrieve the connection URI. With the subarctic python module, it is possible to:
- Create a collection
- Delete a collection
- Insert data into a collection, from .csv file

The user only needs to import subarctic into his/her script without dealing with low-level pymongo library.

### How to:

#### VR and Data Collection
1. On the HoloLens2, install an application. For our purposes, we loaded Basket Bin, an application that scans your environment and implements a VR basket and paper balls, and the user has 30 seconds to shoot the paper balls into the basket. Ideally, the selected application will be one in which the user has to move around, exerting a small-to-moderate amount of physical activity.
2. The user must connect to the physiological sensors, and record data while the activity is being performed.
3. Collect all data. Supported filetypes for the script is .csv

#### Data Framework / Storage
1. Clone this repositorty, and navigate to the directory the files are stored.
2. ....... update .....
3. ....... update .....
