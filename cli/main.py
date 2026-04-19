import click

@click.group()
def cli():
    """Main entry point for the Jarvis CLI."""
    pass

@cli.command()
def init():
    """Initialize Jarvis configuration."""
    click.echo('Jarvis initialized!')

@cli.command()
@click.argument('query')
def ask(query):
    """Ask a question to Jarvis."""
    click.echo(f'You asked: {query}')

@cli.command()
def doctor():
    """Run diagnostics on Jarvis."""
    click.echo('Running diagnostics...')

@cli.command()
def serve():
    """Serve the Jarvis application."""
    click.echo('Serving Jarvis...')

@cli.command()
@click.argument('message')
def chat(message):
    """Chat with Jarvis."""
    click.echo(f'Chatting with Jarvis: {message}')

if __name__ == '__main__':
    cli()