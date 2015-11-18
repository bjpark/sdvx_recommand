sdvx_recommand
==============
SoundVoltex 2,3 Song recommand Library.

*NOTE : This library doesn't support SDVX1.

Usage
-----
* MUST DOWNLOAD SDVX2,3's ALBUM ART!!
  * Download album art to use downPng.py.
* `get_song` gets 2 arguments : `(lev, version)`
  * `lev` : Int, Insert Song's Level. (13, 14, 15, 16)
  * `version` : Int, Insert Song's Version. (2, 3)
  
Example
-------
```python
>>> import sdvxrec
>>> print getSong(15,2)
...
received level is 15
received version is 2
sdvx version is 2
page is 47
selected page is 12
-----------------------------------------------------
Founded Level is 15
User requested level is 15
User requested level is 2
XROSS INFECTION
-----------------------------------------------------
15
XROSS INFECTION
{'sdvx_ver': 2, 'page': 12, 'idx': 3, 'title': u'XROSS INFECTION'}
```
Enjoy!
