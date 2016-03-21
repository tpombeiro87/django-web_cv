# django-web_cv

This is a django single page that renders a curriculum that can be customized using django admin.

It has multiple personalized sections:
* Style
* Contact references
* Education 
* Languages spoken
* Interests
* Skills
* Biography
* Working Experiences

Print screens:

<img src="https://github.com/tpombeiro87/django-web_cv/blob/master/example_1.png?raw=true" width="400">
<img src="https://github.com/tpombeiro87/django-web_cv/blob/master/example_2.png?raw=true" width="400">




In order to edit access url: /admin
    username: user
    password: CV_12345
You can edit the user and the "Me" object in order to interact personalize the cv.


In order to view the cv just access url: /web-cv/view.html

Suggestions:
* Use python 2.7 (not tested for other versions)
* Use Django version 1.9.4 (not tested for other versions)

To play around with a demo version you can check this link: 
[demo](http://tpombeiro87.pythonanywhere.com/web-cv/tp.html)
(all changes made will be lost everyday at 00:00 UTC - a reset to the demo database is done)

# To install

sudo bash #(if necessary)

cd web_cv
pip install -r requirements.txt 


# Credits

## Special thanks
To [Xiaoying Riley](http://themes.3rdwavemedia.com/) for providing the css design. more info about it [here / webpage](http://themes.3rdwavemedia.com/website-templates/orbit-free-resume-cv-template-for-developers/) or [here / git](https://github.com/xriley/Orbit-Theme) 

## Done by
Tiago Pombeiro tpombeiro87@gmail.com


# Todos

* Support Multi cv's
* Picture upload dynamic
* Multi-language support
* Project section
* Integrate with Linkdin
* Integrate with multiple other css templates
* Set all links to open in a new page
* Password protected cv

