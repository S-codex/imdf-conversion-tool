import sys
from pathlib import Path
import json
from dataclasses import asdict
from unit.unit import Unit
from unit.geometry import Geometry
from unit.display_point import DisplayPoint
from unit.properties import Properties
from unit.features import Features

def __map_unit(unit_dict : dict) -> dict:
    features = []
    if 'features' in unit_dict:
        for feat in unit_dict.get('features'):
            feature = Features(feature_type="unit")

            # create geometry object if it exists in input
            geometry = None
            if 'geometry' in feat and feat.get('geometry'):
                geometry = Geometry()
                if 'coordinates' in feat['geometry']:
                    coords = feat['geometry']['coordinates']
                    if coords and type(coords) is list:
                        geometry.coordinates=feat['geometry']['coordinates'][0]

            if geometry:
                feature.geometry = geometry

            # create properties object if it exists in input
            properties = None
            if 'properties' in feat and feat.get('properties'):
                properties = Properties()
                properties.name=feat['properties'].get('name')
                properties.alt_name=feat['properties'].get('alt_name')
                properties.category=feat['properties'].get('category')
                properties.restriction=feat['properties'].get('restriction')
                properties.level_id=feat['properties'].get('level_id')

                # create display_point object if it exists in input
                display_point = None
                if 'display_point' in feat['properties'] and feat.get('properties').get('display_point'):
                    display_point = DisplayPoint()
                    display_point.coordinates=feat['properties']['display_point'].get('coordinates')

                if display_point:
                    properties.display_point=display_point

                # rest of feature keys mapping
                feature.id=feat['properties'].get('id')

            if properties:
                feature.properties = properties

            features.append(feature)

    unit = Unit()
    unit.type = unit_dict.get('type')
    unit.name = unit_dict.get('name')
    if features :
        unit.features = features

    return asdict(unit)


def convert_unit(inFilePath, outFilePath) :
    try:
        print("reading Unit input file ...")
        with open(inFilePath, "r") as in_unit_file:
            unit_dict_in = json.load(in_unit_file)
            print("Successfully read Unit input file!")
    except FileNotFoundError as e:
        print(f"Error : {e.strerror} : \"Input File '{e.filename}' does not exist. Please enter a valid file path/name.\"")

        raise SystemExit

    unit_imdf_dict = __map_unit(unit_dict_in)
    unit_imdf_json = json.dumps(unit_imdf_dict, indent=4)
    # print(venue_imdf_json)

    out_path_obj = Path(outFilePath)
    out_path_obj.resolve().parent.mkdir(parents=True, exist_ok = True)
    with out_path_obj.open(mode='w') as out_file:
        print("writing to Unit output file ...")
        out_file.write(unit_imdf_json)
    print("Successfully wrote Unit to output file!\n"+"-"*50)


def __main():
    args = sys.argv[1:]
    try:
        inFilePath = args[0]
        outFilePath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input file and Output file, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\n Unit Conversion started.")

    convert_unit(inFilePath, outFilePath)

if __name__ == "__main__":
    __main()