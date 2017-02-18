"""
This is a sample module that does stuff. You can use reST to mark up
all sorts of stuff. For example, here's some code

::

    from __future__ import print_function
    print('I\'m a python! hissssssssss!')

And here's a table:

+-------------+-------------+
| Heading One | Heading Two |
+-------------+-------------+
| Row One     | Row One     |
| Row Two     | Row Two     |
+-------------+-------------+

----

Here's a field list

:Authors:
    Nikhil Anand, Salazar Slytherin
:Something Else:
    Random text
"""


def hello_world(name='Nikhil'):
    """A sample function

    :param name: The name to greet with a "Hello"!
    :param another_param: Another parameter

    When imported from another module::

        hello_world('Foobar')

    That's all there is!
    """
    return 'Hello, {}!'.format(name)


class SampleClass():
    """This is a sample class. Here's how you would use it:
    ::

        from my_python_library import sample_module
        a = sample_module.SampleClass('p', 'q')
    """

    def sample_method(a, b, c=None):
        """This is a method in the sample class

        :param a: First parameter
        :param b: Second parameter
        :param c: Third parameter
        """
