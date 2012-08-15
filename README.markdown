# Kraki

A command-line interface to Rolf.

## Install

    $ virtualenv ve
    $ ./ve/bin/pip install git+https://github.com/ccnmtl/kraki.git


Once it's installed, the first thing you need to do is configure Kraki
and set up an API_KEY. 

Log into your Rolf instance and navigate to `/api/1.0/get_key/`

It will look something like this:

![API Key Generation](https://github.com/ccnmtl/kraki/raw/master/api_gen.png)

Pick one or the other of the keys available. 

Create a `~/.kraki_config.txt` file on your machine. Put the following
in it:

    ROLF_BASE = https://rolf.example.com
    API_KEY = eyJ1c2VybmFtZSI6ImFucDgifQ.Aw17lA.9BZIFeo4TvFZJLwh1HvZfMWhFZc

(though, obviously with the base url for your system and your actual
api key). 

Next, you will need to know the deployment id for the deployment you
want to push. The easiest thing to do is to just navigate to the
desired deployment page in the browser and look at the URL. (hint:
it's the number part). 

Then, you should be able to run:

    $ ./ve/bin/python kraki.py push 1234

And see some output. A successful run of a trivial test deployment
might look something like this:

    === STAGE: noop ===
    Stage succeeded
    --- Command ---
    >>> if [ "$CHECKOUT_DIR" = "" ]; then
    >>>    echo "checkout dir not set!"
    >>> else
    >>>    rm -rf $CHECKOUT_DIR
    >>> fi
    === STAGE: blah ===
    Stage succeeded
    === STAGE: echo test ===
    Stage succeeded
    --- Command ---
    >>> echo "hello there."
    >>> echo "here is some output to test formatting with"
    >>> echo "and some error output too" >&2
    --- STDOUT ---
        hello there.
        here is some output to test formatting with
    --- STDERR ---
        and some error output too
