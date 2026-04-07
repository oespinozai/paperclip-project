import argparse


def build_message(project_name: str = "Paperclip project", uppercase: bool = False) -> str:
    message = f"{project_name} initialized"
    if uppercase:
        return message.upper()
    return message


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print the project initialization message.")
    parser.add_argument(
        "--project-name",
        default="Paperclip project",
        help="Project name used in the initialization message.",
    )
    parser.add_argument(
        "--uppercase",
        action="store_true",
        help="Print the initialization message in uppercase.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None):
    if argv is None:
        argv = []
    args = parse_args(argv)
    print(build_message(project_name=args.project_name, uppercase=args.uppercase))


def run_cli():
    args = parse_args()
    print(build_message(project_name=args.project_name, uppercase=args.uppercase))


if __name__ == "__main__":
    run_cli()
