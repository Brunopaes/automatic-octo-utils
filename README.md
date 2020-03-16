## hu3: Helpers and Utils functionalities

Optimized for python 3.6

Utils repository. Functions used in daily routines.

----------------------

### Project's Structure

```bash 
.
└── automatic-octo-utils
    ├── data
    │   └── settings.json
    ├── docs
    │   └── CREDITS
    ├── src
    │   ├── __init__.py
    │   ├── helpers.py
    │   ├── messaging.py
    │   └── setup.py
    ├── tests
    │   └── unittests
    │       ├── __init__.py
    │       ├── test_helpers.py
    │       └── test_messaging.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── requirements.txt
```

#### Directory description

- __data:__ The data dir. Group of non-script support files.
- __docs:__ The documentation dir.
- __src:__ The scripts & source code dir.
- __tests:__ The unittests dir.

-----------------------

### Usage Notes

#### Running

For running it, run the follow command:
````shell script
pip install hu3
````

After installing, just import it as a python module in your project.

```python
from hu3 import messaging
```

### Roadmap

This project is under development.

<table>
    <tr><td colspan="2">
      Python
      <br/><small><i>Roadmap</i></small>
    </td></tr>  
    <tr>
      <td><small>0.1.0</small></td>
      <td><small>2020-03-11</small></td>
      <td width="350"><small><small>helpers.read_json, messaging.mail</small></small></td>
    </tr>
    <tr>
      <td><small>0.1.1</small></td>
      <td><small>2020-03-16</small></td>
      <td width="350"><small><small>name changes</small></small></td>
    </tr>
</table>

---------------