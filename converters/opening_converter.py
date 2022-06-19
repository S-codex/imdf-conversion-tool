import sys
from pathlib import Path
import json
from dataclasses import asdict
from opening.door import Door
from opening.opening import Opening
from opening.display_point import DisplayPoint
from opening.properties import Properties
from opening.geometry import Geometry
from opening.features import Features


def __map_opening(opening_dict: dict) -> dict:
    features = []
    if 'features' in opening_dict:
        for feat in opening_dict.get('features'):
            feature = Features(feature_type="opening")

            # create geometry object if it exists in input
            geometry = None
            if 'geometry' in feat and feat.get('geometry'):
                geometry = Geometry()
                if 'coordinates' in feat['geometry'] and feat['geometry']['coordinates'] and type(feat['geometry']['coordinates']) is list:
                    geometry.coordinates = feat['geometry']['coordinates'][0]


            if geometry:
                feature.geometry = geometry

            # create properties object if it exists in input
            properties = None
            if 'properties' in feat and feat.get('properties'):
                properties = Properties()
                properties.category = feat['properties'].get('category')
                properties.accessibility = feat['properties'].get(
                    'accessibility')
                properties.access_control = feat['properties'].get(
                    'access_control')
                properties.name = feat['properties'].get('name')
                properties.alt_name = feat['properties'].get('alt_name')
                properties.level_id = feat['properties'].get('level_id')

                # create door object if it exists in input
                door = None
                if 'door' in feat['properties'] and feat.get('properties').get('door'):
                    door = Door()
                    door.automatic = feat.get('properties').get(
                        'door').get('automatic')
                    door.material = feat.get('properties').get(
                        'door').get('material')
                    door.type = feat.get('properties').get('door').get('type')
                properties.door = door

                # create display_point object if it exists in input
                display_point = None
                if 'display_point' in feat.get('properties') and feat.get('properties').get('display_point'):
                    display_point = DisplayPoint()
                    display_point.coordinates = feat.get('properties').get('display_point').get(
                        'coordinates')
                properties.display_point = display_point

                # rest of feature keys mapping
                feature.id = feat['properties'].get('id')

            if properties:
                feature.properties = properties

            features.append(feature)

    opening = Opening()
    opening.type = opening_dict.get('type')
    opening.name = opening_dict.get('name')
    if features:
        opening.features = features

    return asdict(opening)


def convert_opening(inFilePath, outFilePath):
    try:
        print("reading Opening input file ...")
        with open(inFilePath, "r") as in_opening_file:
            opening_dict_in = json.load(in_opening_file)
            print("Successfully read Opening input file!")
    except FileNotFoundError as e:
        print(
            f"Error : {e.strerror} : \"Input File '{e.filename}' does not exist. Please enter a valid file path/name.\"")

        raise SystemExit

    opening_imdf_dict = __map_opening(opening_dict_in)
    opening_imdf_json = json.dumps(opening_imdf_dict, indent=4)
    # print(opening_imdf_json)

    out_path_obj = Path(outFilePath)
    out_path_obj.resolve().parent.mkdir(parents=True, exist_ok=True)
    with out_path_obj.open(mode='w') as out_file:
        print("writing to Opening output file ...")
        out_file.write(opening_imdf_json)
    print("Successfully wrote Opening to output file!\n"+"-"*50)


def __main():
    args = sys.argv[1:]
    try:
        inFilePath = args[0]
        outFilePath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input file and Output file, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\n Opening Conversion started.")

    convert_opening(inFilePath, outFilePath)


if __name__ == "__main__":
    __main()
