# 0xTables  <img width="60px" src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif">

A handy package to draw ASCII tables easily and effortlessly.

# Installation :

From pip :

```bash
pip3 install oxtables
```

From source :

```bash
git clone https://github.com/0x68616469/oxtables/
```

# Example :

```python
from oxtables import Table

th = Table(style="-",
           border_color="black",
           text_color="white",
           align="left",
           spacer=True, 
           first_row="default",
           max_length=50)

th.add(["Argument", "Description", "Default"])
th.add(["style", "Change border ascii style", "-"])
th.add(["border_color", "Change the border color", "black"])
th.add(["text_color", "Change the text color", "white"])
th.add(["align", "Text align (left/center/right)", "left"])
th.add(["spacer", "Print the spacer between rows (True/False)", "True"])
th.add(["first_row", "Change first row styling (border/side/none/default)", "default"])
th.add(["max_length", "Max text length", "50"])

th.draw()
```

Result :

<img src="https://media.giphy.com/media/fG3B9uLAfU2WnEp1kE/giphy.gif">

<hr>

![Follow me](https://img.shields.io/badge/-Follow%20Me-222222?logo=twitter&logoColor=black&color=272838&labelColor=C09891&style=for-the-badge&logoWidth=30&link=https://twitter.com/0x68616469)