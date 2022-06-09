import sys

from venue_converter import convert_venue


def __main():
    args = sys.argv[1:]
    try:
        inFilePath = args[0]
        outFilePath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input Directory and Output Directory, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\nConversion started.")

    convert_venue(inFilePath, outFilePath)

if __name__ == "__main__":
    __main()