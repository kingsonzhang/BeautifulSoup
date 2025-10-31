# SWE262 Programming Styles Repository by Kingson Zhang

## Milestone 2 Project Directions

<p>First, create and activate a virtual environment for the Milestone project</p>
<p>Instructions below are for Windows machines only</p>

```bash
BeautifulSoup:~/ python -m venv venv
BeautifulSoup:~/ Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
BeautifulSoup:~/ ./venv/Scripts/activate    # On Windows to activate the virtual environment
(venv) BeautifulSoup:~/ pip install -e .
(venv) BeautifulSoup:~/ pip install pytest
(venv) BeautifulSoup:~/ deactivate                 # On Windows to deactivate the cirtual environment
```

<p> Activate the virtual environment again before running the tasks for Milestone 2</p>

```bash
BeautifulSoup:~/ ./venv/Scripts/activate    # On Windows to activate the virtual environment
```

## Part 2
<p>Change Directory into m2 to begin running the tasks</p>

```bash
BeautifulSoup:~/ cd ./apps/m2
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
(venv) BeautifulSoup\apps\m2:~/ python task4.py "../Websites/BeautifulSoup.html"
(venv) BeautifulSoup\apps\m2:~/ python task5.py "../Websites/SimpleWebpage.html"
(venv) BeautifulSoup\apps\m2:~/ python task6.py "../Websites/UCIrvine.html"
```

## Part 3

<p>Currently Part 3 is not working correctly. I have made changes to the source code, and will be attempting to fix the issues <br>
Once the fixes are implemented, the README will be updated to reflect the changes. For now, task6.py can be ran, but the output is incorrect
</p>

```bash
(venv) BeautifulSoup\apps\m2:~/ python task6.py "../Websites/BeautifulSoup.html"
```