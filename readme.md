## lgl - python packaging manager launcher

libgirl launcher is a packaging manager to create python project

![lgl demo](lgl_demo.gif)

## Installation

```
pip install lgl
```

## Features

* Create project directory.
* Find lacking packge and install after analyze source code.
* manage `import` forms for the package.
* Launch application.

## Usage

```
$ lgl
usage: lgl [-h] {run,install,fmt,init} ...

positional arguments:
  {run,install,fmt,init}
    run                 see `run -h`
    install             see `install -h`
    fmt                 see `fmt -h`
    init                see `init -h`

optional arguments:
  -h, --help            show this help message and exit
```

    $ lgl init project-name # create project directory
    $ lgl install           # install depending libraries.
    $ lgl fmt               # manage `import` forms
    $ lgl run [arguments]   # launch application

## Author
Team Libgirl(team@libgirl.com)

## License
Licensed under the Apache License 2.0 License.
