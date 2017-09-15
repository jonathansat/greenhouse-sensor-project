Just another basic Python project representing a greenhouse system in software.

No dependencies, nothing crazy, just pure Python.

To run:

.. code-block:: python

        ./main.py

TODO
----
In order of increasing difficulty and sensibly ordered to incrementally build things:

* Create more kinds of sensors representative of what you'd find in a small/medium scale commercial greenhouse
* Create a way to persist/store the sensor values
* Allow new sensor instances to be added to the system dynamically (e.g. by a user)
* Store sensor instance info in a config file of some sort so they can be persisted/restored
* Display sensor information in a very basic web application (e.g. with Flask and Bootstrap)
* Create an event system that reacts to sensor values (for extra points if it reacts to value ranges)
* Expand the event system to allow for different kinds of notifications:

  * print to stdout
  * make beep sounds
  * email

* Expand the web application to include all the above functionality (hard mode!: UX/UI)
