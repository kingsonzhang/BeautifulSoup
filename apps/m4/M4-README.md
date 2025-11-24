# Milestone-4

## Milestone 4 Project Directions

<p>The virtual environment has already been setup, so we only need to activate it again before running the program.</p>

```bash
# On Windows to activate the virtual environment
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
./venv/Scripts/activate
```

<p>For Milestone 4, all that was needed was to create an __iter__ function inside BeautifulSoup to make BeautifulSoup an iterable</p>
<p>Once that has been created, BeautifulSoup will now return the HTML page as an iterable.</p>
<p>Once again, any of the previous HTML pages provided can be used as an argument to test Milestone 4</p>

```bash
cd ./apps/m4
python milestone4.py "../Websites/BeautifulSoup.html"
```