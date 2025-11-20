# SWE262 Programming Styles Repository by Kingson Zhang

## Milestone 3 Project Directions

<p>The virtual environment has already been setup, so we only need to activate it again before running the program.</p>

```bash
# On Windows to activate the virtual environment
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
./venv/Scripts/activate
```

<p>For Milestone 3, I've editted the replacer class to allow 3 additional parameters to be passed<br>
<ul>
<li>name_xformer: Pass in a lambda function that takes a tag, and returns a new name if the tag name should be changed. Default value None.
<li>attrs_xformer: Pass in a lambda function that takes a tag, and returns a new attribute if the tag attribute should be changed. Default value None.
<li>xformer: Pass in a lambda function that takes a tag, and the lambda function will change properties about the tag without returning anything. Default value None.
</ul>
</p>
<p>In addition, the old tag and new tag parameters have been changed to a tuple (oldTag, newTag). Default value None.<br>
SoupReplacer do not act as a filter unless this parameter has been passed a tuple.
</p>
<p>
Task 7 from Milestone 1 has been rewritten. Using SoupReplacer, it filters out all the elements with tag "b", and adds an attribute to the element.
</p>

```bash
cd ./apps/m3
python task7.py "../Websites/BeautifulSoup.html"
```