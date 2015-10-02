To use any of the samples you have to install the Devicehub.net C library:

    $ sudo apt-get install libssl-dev
    $ git clone http://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.c.git
    $ cd org.eclipse.paho.mqtt.c.git
    $ make
    $ sudo make install
    $ sudo apt-get install cmake
    $ git clone https://github.com/devicehubnet/devicehub_c.git
    $ cd devicehub_c.git
    $ mkdir build
    $ cd build
    $ cmake..
    $ make
    $ sudo make install

To run the included sample (be sure to be in the build folder)::

    $ ./devicehub_test
