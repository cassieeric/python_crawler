[Introduction]

This folder is used to crawler data from http://www.icbase.com/.
The main fucntion is to collect the all website data.

[Strategy]
Using requests+re+xpath modules.
Firstly, we collect the second website tags.
Then, base on the second website tags, we collect the third website tags.
Next, we store the collected urls in a txt file named all_urls.txt file.
Finally, we collect the detail info based on the urls in the txt file and import into excel.
