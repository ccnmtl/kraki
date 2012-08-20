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

    $ ./ve/bin/kraki push 1234

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

## Future Development

If you want to pitch in, these areas are all in need of help:

* Currently, "push" is the only supported action. Would be nice to be
  able to query stuff, do rollbacks, etc.
* This is not heavily tested yet. Don't use it if you don't think you
  can help debug it.
* particularly, the config file and argument parsing are not robust
* Is 7 days a good duration for timed keys? Thoughts?
* two-way key generation handshake? ie, you run kraki on the
  commandline without an API key, it generates a random hash, sends
  you to a rolf URL that uses that random hash along with your
  username to generate a token. That would allow us to generate tokens
  that aren't directly tied to an IP address. Still thinking about how
  this should all work to be as smooth as possible without opening up
  gaping security holes.
