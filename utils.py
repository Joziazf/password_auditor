from rich.console import Console
from rich.table import Table
from analyzer import PasswordReport

console = Console()

def display_report(report: PasswordReport) -> None:
    table = Table(title="Password Analysis")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="white")

    table.add_row("Length", str(report.length))
    table.add_row("Uppercase", "✓" if report.has_uppercase else "✗")
    table.add_row("Lowercase", "✓" if report.has_lowercase else "✗")
    table.add_row("Digits", "✓" if report.has_digits else "✗")
    table.add_row("Special chars", "✓" if report.has_special else "✗")
    table.add_row("Score", f"{report.score}/6")

    strength_color = {
        "weak": "red",
        "medium": "yellow",
        "strong": "green"
    }
    color = strength_color.get(report.strength, "white")
    table.add_row("Strength", f"[{color}]{report.strength}[/{color}]")

    console.print(table)