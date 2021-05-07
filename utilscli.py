#!/usr/bin/env python
import click
import requests

@click.group()
@click.version_option("1.0")
def cli():
    """Machine Learning Utility Belt"""




@cli.command("index")
@click.option("--host", default="http://127.0.0.1:5000/", help="Host to query")
def mkrequest(host):
    """Sends prediction to ML Endpoint"""
    
    click.echo(click.style(f"Accessing the server",
        bg="green", fg="white"))

    result = requests.get(url=host)
    click.echo(click.style(f"result: {result.text}", bg="red", fg="white"))


if __name__ == "__main__":
    cli()