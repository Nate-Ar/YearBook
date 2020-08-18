# Online Year Book
## Geting Started
First, make sure you have python3 installed<br>
Second, install Flask using pip `pip3 install flask`<br>
Third, Donwload the files and run the python file `python3 page.py`<br>
Fourth, go to `http://localhost:5000/` in your browser
## Editing The page
To Change the People in yor year book navigate to the static folder then to the Year folder then you can open any file and change the text inside<br>
The syntax is `Full_Name,Img,Quote,Year` make sure the first entry has the year. Add your images to the images folder also located in the static folder <br>
Make sure to leave the top line there it defines each string<br>
To change what year populates the page after your click a button go to the `page.py` and change the `whaty` varable 0-4<br>
You can add a year by creating a csv file and adding `Full_Name,Img,Quote,Year` at the top of the file and the range the `whaty` varable will still start at 0 but add 1 for every file you add<br>
You Have to stop the program and restart it for the changes to take place<br>
In the future the `whaty` varable will change automatically 
