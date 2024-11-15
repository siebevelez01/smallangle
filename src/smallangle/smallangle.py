"""Program that can be accessed using terminal commands and will print a list of angles
and their sine or tangent values between 0 and 2π for a given number of values in this range.
"""
import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Amount of values between 0 and 2π.",
    show_default=True, # show default in help
)
def sin(number):
    """Print a list of angles and their sine values between 0 and 2π for a given number of values in this range.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="Amount of values between 0 and 2π.",
    show_default=True, # show default in help
)
def tan(number):
    """Print a list of angles and their tangent values between 0 and 2π for a given number of values in this range.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()