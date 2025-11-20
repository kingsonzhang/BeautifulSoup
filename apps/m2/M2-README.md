# SWE262 Programming Styles Repository by Kingson Zhang

## Milestone 2 Project Directions

<p>First, create and activate a virtual environment for the Milestone project</p>
<p>Instructions below are for Windows machines only</p>

```bash
python -m venv venv
# On Windows to activate the virtual environment
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
./venv/Scripts/activate
pip install -e .
pip install pytest
# On Windows to deactivate the cirtual environment
deactivate                 
```

<p> Activate the virtual environment again before running the tasks for Milestone 2</p>

```bash
./venv/Scripts/activate    # On Windows to activate the virtual environment
```

## Part 1
<p>Change Directory into m2 to begin running the tasks</p>

```bash
cd ./apps/m2
```

<p>From here, you can test out the 3 different tasks, seperated into task2.py, task3.py, and task4.py <br>
The HTML websites are included in a folder called Websites on the same level as m2
</p>
<ol>
    <li>APNews</li>
    <li>Archive</li>
    <li>BeautifulSoup</li>
    <li>NYSE</li>
    <li>Reddit</li>
    <li>Reuters</li>
    <li>SimpleWebpage</li>
    <li>TechCrunch</li>
    <li>UCIrvine</li>
    <li>Wikipedia</li>
</ol>

```bash
python task4.py "../Websites/BeautifulSoup.html"
python task5.py "../Websites/SimpleWebpage.html"
python task6.py "../Websites/UCIrvine.html"
```

## Part 2
<p>A lot of the API calls made in the previous tasks come from files found in the bs4 folder. <br>
BeautifulSoup class can be found in the __init__.py file.<br>
SoupStrainer class can be found in the filter.py file.<br>
The HTML parser itself, such as lxml, can be found in the folder builder, and the file called _htmlparser.py
</p>

## Part 3

<p>Milestone 2 is now working! Sorry for the wait. I finally understand what is going on in the code and fixed most of the issues.<br>
The SoupReplacer class is a SoupStrainer class, meaning it will only filter out the parts of the HTML that we want.<br>
On top of filtering out the requested parts, it will change the requested tags into the new tag passed as an argument.<br>
For Task 6, I currently have it set to filter out all the "b" elements, and replace all "b" elements with "blockquote".<br>
You can run task6.py with any of the 10 provided HTML files.
</p>

```bash
python task6.py "../Websites/BeautifulSoup.html"
```