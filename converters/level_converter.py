import sys
from pathlib import Path
import json
from distutils.util import strtobool
from dataclasses import asdict
from level.level import Level
from level.display_point import DisplayPoint
from level.properties import Properties
from level.geometry import Geometry
from level.features import Features

def __map_level(level_dict : dict) -> dict:
    features = []
    if 'features' in level_dict:
        for feat in level_dict.get('features'):
            feature = Features(feature_type="level")

            # create geometry object if it exists in input
            geometry = None
            if 'geometry' in feat and feat.get('geometry'):
                geometry = Geometry()
                if 'coordinates' in feat['geometry']:
                    coords = feat['geometry']['coordinates']
                    if coords and type(coords) is list:
                        # FIXME: find the correct structure of coords b/w two formats. list-convert them in a better way.
                        geometry.coordinates=feat['geometry']['coordinates'][0]


            if geometry:
                feature.geometry = geometry

            # create properties object if it exists in input
            properties = None
            if 'properties' in feat and feat.get('properties'):
                properties = Properties()
                properties.category=feat['properties'].get('category')
                properties.restriction=feat['properties'].get('restriction')
                properties.outdoor=bool(strtobool(feat['properties'].get('outdoor')))
                properties.ordinal=feat['properties'].get('ordinal')
                properties.name=feat['properties'].get('name')
                properties.short_name=feat['properties'].get('short_name')
                properties.address_id=feat['properties'].get('address_id')
                properties.building_ids=feat['properties'].get('building_ids')

                # create display_point object if it exists in input
                display_point = None
                if 'display_point' in feat.get('properties') and feat.get('properties').get('display_point'):
                    display_point = DisplayPoint()
                    display_point.coordinates=feat['properties']['display_point'].get('coordinates')

                if display_point:
                    properties.display_point=display_point

                # rest of feature keys mapping
                feature.id=feat['properties'].get('id')

            if properties:
                feature.properties = properties

            features.append(feature)

    level = Level()
    level.type = level_dict.get('type')
    level.name = level_dict.get('name')
    if features :
        level.features = features

    return asdict(level)


def convert_level(inFilePath, outFilePath) :
    try:
        print("reading Level input file ...")
        with open(inFilePath, "r") as in_level_file:
            level_dict_in = json.load(in_level_file)
            print("Successfully read Level input file!")
    except FileNotFoundError as e:
        print(f"Error : {e.strerror} : \"Input File '{e.filename}' does not exist. Please enter a valid file path/name.\"")

        raise SystemExit

    level_imdf_dict = __map_level(level_dict_in)
    level_imdf_json = json.dumps(level_imdf_dict, indent=4)

    out_path_obj = Path(outFilePath)
    out_path_obj.resolve().parent.mkdir(parents=True, exist_ok = True)
    with out_path_obj.open(mode='w') as out_file:
        print("writing to Level output file ...")
        out_file.write(level_imdf_json)
    print("Successfully wrote Level to output file!\n"+"-"*50)


def __main():
    args = sys.argv[1:]
    try:
        inFilePath = args[0]
        outFilePath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input file and Output file, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\n Level Conversion started.")

    convert_level(inFilePath, outFilePath)

if __name__ == "__main__":
    __main()