<h1>Note that your assets that is your csv files are stored in a directory called "assets"</h1>
<h1>
Setting up your environment
</h1>



<h1>1. Install python 3.7.3</h1>

In the installation, your installer will ask something similar to "ADD PATH IN THE ENVIRONMENT VARIABLE" ,make sure that option is ticked.

After sucessfully installing python verify if you're able to use it in your command prompt. Do this by typing "CMD" in your windows search without the quotations. After your command prompt open up, type "python" without quotations. If you run into an error, then 
you probably didn't added python to your path. 
<a href = "https://datatofish.com/add-python-to-windows-path/">Here's a good tutorial that covers this topic.</a>


<h1>2. Get pip for installing additional libraries</h1>

<a href = "https://bootstrap.pypa.io/get-pip.py"> Get get-pip file from this website</a>
Copy all the contents into a .py file extension using a text editor and rename the file get-pip.py
Paste it in your desktop. 

<h1>3. Install get-pip</h1>
Open your cmd and then use commands
cd desktop
python get-pip.py

to let python intall get-pip.py file for you.

<h1>4. Installing dependencies via pip</h1>
Go into your project folder using cmd and type "pip install -r requirements.txt" to setup your coding environment. Now youre reading to run the scraper!



<h1>A. Running the tmppro.com scraper</h1>

<h2>To run the scraper type "idle" in your windows search. When idle opens up, click on file > open. And open your main.py file. Once it opens up, press F5 to run the file.</h2>
<p>
Finally type main() to run the scraper, your results will automatically get saved in assets/products1.csv file. Make sure to not open that file while the scraper is running and instead copy the csv file to some other location and open that copy to check if the scraper is getting the correct data.


