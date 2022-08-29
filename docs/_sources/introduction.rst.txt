Introduction
============

Very often when filming you need an extra spotlight to adjust lighting or when camping you need a flashlight, torch or headlight. CircuitPython spotlight are various scripts made for specific CircuitPython boards to learn how each board works and can be used to teach new users to Python, CircuitPython, electronics and some core programming concepts as well.

Available boards
----------------
Below is a list of boards which spotlights have been made for

- [X] Circuit Playground Bluefruit

- [X] Circuit Playground Express

- [ ] BBC Micro Bit

- [ ] MagTag

- [ ] Matrix Portal


Contributing
------------
Pull requests, corrections, translations & fixes are welcome. Any contributions must be submitted under the same license that the original piece of work (see below). Take a look at any open issues or submit new ones if there is something that needs to be fixed or added.

Watch our video on how to contribute to open source for a complete overview -> `https://www.youtube.com/watch?v=UWA4wyacY2A <https://www.youtube.com/watch?v=UWA4wyacY2A>`__

Building the sphinx docs
------------------------
After cloning the repository if you wish to edit or make improvements to it, you need to edit the relevant files in the :code:`docs_source` folder and when you want to build it, you run the following command from the root folder of the repository. The output will then be able to be opened locally from the :code:`docs` folder.
::
 sphinx-build docs_source/source docs
