# resizr
> An extremely simple image resizer built using Google App Engine

## Usage 

*URL* - ``'http://im-resizr.appspot.com/img/w:<width>h:<height>?url=<url>```

## Example

Image URL - `https://github.com/iamareebjamal/resizr/blob/master/image/android-image.png?raw=true`

Size - *1.27 MB* - (1920x1080)


- Resize (width only) : `http://im-resizr.appspot.com/img/w:500h:0?url=https://github.com/iamareebjamal/resizr/blob/master/image/android-image.png?raw=true`  
![](http://im-resizr.appspot.com/img/w:500h:0?url=https://github.com/iamareebjamal/resizr/blob/master/image/android-image.png?raw=true)  

Size - *97.4 KB* - (500x281)

*Notice the 0 in h <height> argument*

- Resize (Height only) : `http://im-resizr.appspot.com/img/w:0h:500?url=https://github.com/iamareebjamal/resizr/blob/master/image/android-image.png?raw=true`  
![](http://im-resizr.appspot.com/img/w:0h:500?url=https://github.com/iamareebjamal/resizr/blob/master/image/android-image.png?raw=true)  

Size - *320 KB* - (889x500)

- Resize (Best Fit) : You get the idea :wink:

## Features

- Fixed aspect ratio of images
- Both server side and client side caching

## Authors

[@iamareebjamal](https://github.com/iamareebjamal)
