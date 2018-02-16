WHAT IS IT?

This is a python script which uses BeautifulSoup and GitPython libraries which automatically clones all the repositories listed by the user in an xml file to appropriate location and proper branches.

HOW TO USE IT?

The use of this tool is very simple. All you have to do is edit the manifest.xml.tempelate file according to your own use (for eg. https://github.com/Exynos7870/PyClone/commit/12a9ccc748c0e7b0a26c3e92fd80c63d59699e3e ) , and rename it to manifest.xml. And install all the dependencies, i.e BeautifulSoup4 and GitPython. For installing the dependencies just run the setupenv.sh script as:
>> ./setupenv.sh

Done.

Now all you have to do is running the following command:
>> python3 main.py
