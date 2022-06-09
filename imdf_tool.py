import sys
from pathlib import Path
from venue_converter import convert_venue
from address_converter import convert_address

def __main():
    args = sys.argv[1:]
    try:
        inDirectoryPath = args[0]
        outDirectoryPath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input Directory and Output Directory, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\nConversion started.")

    for inFile in Path(inDirectoryPath).glob('*.geojson'):
        outFileName = inFile.name.split('.')[0]+'_imdf'+'.geojson'
        outFile = Path(outDirectoryPath,outFileName)
        if inFile.match("venue*"):
            convert_venue(inFile, outFile)
        elif inFile.match("address*"):
            convert_address(inFile, outFile)


if __name__ == "__main__":
    __main()