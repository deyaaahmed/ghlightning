# Github Lightning :zap:

**ghlightning** is a very simple python package to collect all the information that can be collected about the users of the [GitHub](http://github.com) website.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install ghlightning.

```bash
pip3 install lightning
```

## Usage

```python
from ghlightning import Github

test = Github("7azabet") # initializing an object.
test.email # returns the email of object.
test.fetchInfo() # returns all info about user.
test.countryInfo() # returns all info about user country.
test.downloadFollowersPics() # download all followers pictures
# you can specify a path for downloading images
# default is the current path.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
