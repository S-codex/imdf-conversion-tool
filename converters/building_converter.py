import sys
from pathlib import Path
import json
from dataclasses import asdict
from building.building import Building
from building.display_point import DisplayPoint
from building.properties import Properties
from building.features import Features

def __map_building(building_dict : dict) -> dict:
    features = []
    if 'features' in building_dict:
        for feat in building_dict.get('features'):
            feature = Features(feature_type="building")

            feature.geometry = feat.get('geometry')

            # create properties object if it exists in input
            properties = None
            if 'properties' in feat and feat.get('properties'):
                properties = Properties()
                properties.name=feat['properties'].get('name')
                properties.alt_name=feat['properties'].get('alt_name')
                properties.category=feat['properties'].get('category')
                properties.restriction=feat['properties'].get('restriction')
                properties.address_id=feat['properties'].get('address_id')

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

    building = Building()
    building.type = building_dict.get('type')
    building.name = building_dict.get('name')
    if features :
        building.features = features

    return asdict(building)


def convert_building(inFilePath, outFilePath) :
    try:
        print("reading Building input file ...")
        with open(inFilePath, "r") as in_building_file:
            building_dict_in = json.load(in_building_file)
            print("Successfully read Building input file!")
    except FileNotFoundError as e:
        print(f"Error : {e.strerror} : \"Input File '{e.filename}' does not exist. Please enter a valid file path/name.\"")

        raise SystemExit

    building_imdf_dict = __map_building(building_dict_in)
    building_imdf_json = json.dumps(building_imdf_dict, indent=4)
    # print(venue_imdf_json)

    out_path_obj = Path(outFilePath)
    out_path_obj.resolve().parent.mkdir(parents=True, exist_ok = True)
    with out_path_obj.open(mode='w') as out_file:
        print("writing to Building output file ...")
        out_file.write(building_imdf_json)
    print("Successfully wrote Building to output file!\n"+"-"*50)


def __main():
    args = sys.argv[1:]
    try:
        inFilePath = args[0]
        outFilePath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input file and Output file, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\n Building Conversion started.")

    convert_building(inFilePath, outFilePath)

if __name__ == "__main__":
    __main()