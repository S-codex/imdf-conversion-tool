import sys
from pathlib import Path
import json
from dataclasses import asdict
from footprint.footprint import Footprint
from footprint.properties import Properties
from footprint.geometry import Geometry
from footprint.features import Features

def __map_footprint(footprint_dict : dict) -> dict:
    features = []
    if 'features' in footprint_dict:
        for feat in footprint_dict.get('features'):
            feature = Features(feature_type="footprint")

            # create geometry object if it exists in input
            geometry = None
            if 'geometry' in feat and feat.get('geometry'):
                geometry = Geometry()
                if 'coordinates' in feat['geometry']:
                    coords = feat['geometry']['coordinates']
                    if coords and type(coords) is list and type(coords[0]) is list:
                        # FIXME: find the correct structure of coords b/w two formats. list-convert them in a better way.
                        geometry.coordinates=[feat['geometry']['coordinates'][0][0]]

            if geometry:
                feature.geometry = geometry

            # create properties object if it exists in input
            properties = None
            if 'properties' in feat and feat.get('properties'):
                properties = Properties()
                properties.category=feat['properties'].get('category')
                properties.name=feat['properties'].get('name')
                properties.building_ids=feat['properties'].get('building_ids')

                # rest of feature keys mapping
                feature.id=feat['properties'].get('id')

            if properties:
                feature.properties = properties

            features.append(feature)

    footprint = Footprint()
    footprint.type = footprint_dict.get('type')
    footprint.name = footprint_dict.get('name')
    if features :
        footprint.features = features

    return asdict(footprint)


def convert_footprint(inFilePath, outFilePath) :
    try:
        print("reading Footprint input file ...")
        with open(inFilePath, "r") as in_footprint_file:
            footprint_dict_in = json.load(in_footprint_file)
            print("Successfully read Footprint input file!")
    except FileNotFoundError as e:
        print(f"Error : {e.strerror} : \"Input File '{e.filename}' does not exist. Please enter a valid file path/name.\"")

        raise SystemExit

    footprint_imdf_dict = __map_footprint(footprint_dict_in)
    footprint_imdf_json = json.dumps(footprint_imdf_dict, indent=4)
    # print(footprint_imdf_json)

    out_path_obj = Path(outFilePath)
    out_path_obj.resolve().parent.mkdir(parents=True, exist_ok = True)
    with out_path_obj.open(mode='w') as out_file:
        print("writing to Footprint output file ...")
        out_file.write(footprint_imdf_json)
    print("Successfully wrote Footprint to output file!\n"+"-"*50)


def __main():
    args = sys.argv[1:]
    try:
        inFilePath = args[0]
        outFilePath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input file and Output file, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\n Footprint Conversion started.")

    convert_footprint(inFilePath, outFilePath)

if __name__ == "__main__":
    __main()