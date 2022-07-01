import sys
from pathlib import Path
from converters.building_converter import convert_building
from converters.venue_converter import convert_venue
from converters.address_converter import convert_address
from converters.footprint_converter import convert_footprint
from converters.level_converter import convert_level
from converters.opening_converter import convert_opening
from converters.relationship_converter import convert_relationship
from converters.unit_converter import convert_unit


def __main():
    args = sys.argv[1:]
    try:
        inDirectoryPath = args[0]
        outDirectoryPath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input Directory and Output Directory, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\nConversion started.\n")

    for inFile in Path(inDirectoryPath).glob('*.geojson'):
        outFileName = inFile.name.split('.')[0]+'_imdf'+'.geojson'
        outFile = Path(outDirectoryPath, outFileName)
        if "venue" in inFile.name.lower():
            convert_venue(inFile, outFile)
        elif "address" in inFile.name.lower():
            convert_address(inFile, outFile)
        elif "building" in inFile.name.lower():
            convert_building(inFile, outFile)
        elif "footprint" in inFile.name.lower():
            convert_footprint(inFile, outFile)
        elif "level" in inFile.name.lower():
            convert_level(inFile, outFile)
        elif "opening" in inFile.name.lower():
            convert_opening(inFile, outFile)
        elif "relationship" in inFile.name.lower():
            convert_relationship(inFile, outFile)
        elif "unit" in inFile.name.lower():
            convert_unit(inFile, outFile)


if __name__ == "__main__":
    __main()
