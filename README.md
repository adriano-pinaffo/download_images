# download_images
Simple program to download as many images as you want from unsplash.com. You provide the options and the keywords, the program connects to unsplash.com and download the images. Pure and simple.
<pre>
Usage: image-download.py [OPTIONS] Keywords
  -h, --help        Show this help
  -d, --destination Folder to save the files (Default current dir)
  -t, --threads     Number of concurrent downloads (Default ThreadPoolExecutor default)
  -n, --number      Number of images to download (Default 20)
</pre>
  Example:<br>
  python image-download.py -d ~/Pictures -t5 -n10 planets<br>
  Will download 10 images related to the keyword planets using 5 consecutive threads at a time.
  
  <img src="https://github.com/adriano-pinaffo/download_images/blob/master/readme-files/download-images.gif"></img>
