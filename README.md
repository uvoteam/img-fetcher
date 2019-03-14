Image Fetcher
==========

Script parses stdin, finds all urls to images, and then download all images into "output" folder.


    $ echo '<html><body><img src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"</body></html>' | python3 ./img-fetcher.py
