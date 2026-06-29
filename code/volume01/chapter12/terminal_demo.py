import sys


def main() -> int:
    print("Hello from standard output")
    print("Hello from standard error", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
