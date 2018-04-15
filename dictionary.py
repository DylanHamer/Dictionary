#!/usr/bin/python3

"""
Dictionary
Simple command line dictionary
By Dylan Hamer
"""

from PyDictionary import PyDictionary  # English dictionary
import click   # Command line tools

@click.command()
@click.argument("word")  # Word to get meaning for
@click.option("--type", default="Noun")  # Word class, i.e verb
@click.option("--which", default=0)  # Which definition to get if there are multiple meanings
@click.option("--color", default="blue")  # Choose a highlighting color
def dictionary(word, type, which, color):
    dictionary = PyDictionary()  # Initialise dictionary
    meaning = dictionary.meaning(word)  # Get meaning
    if type in meaning.keys():  # Check if the word has the type as a meaning
        click.secho("{}: ".format(word), fg=color, nl=False)  # If it has display the original word in color
        click.echo(meaning[type][which])  # And the meaning
    else:
        click.echo("{} is not a {}.".format(word, type))  # If it doesn't, display an error

if __name__ == "__main__":
    dictionary()  # Run the script
