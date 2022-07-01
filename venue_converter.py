import sys
from pathlib import Path
import json
from dataclasses import asdict
from venue.venue import Venue
from venue.display_point import DisplayPoint
from venue.properties import Properties
from venue.geometry import Geometry
from venue.features import Features

def __map_venue(venue_dict : dict) -> dict:
    features = []
    if 'features' in venue_dict:
        for feat in venue_dict.get('features'):
            feature = Features(feature_type="venue")
            # feature.type=feat.get('type')

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
                properties.hours=feat['properties'].get('hours')
                properties.phone=feat['properties'].get('phone')
                properties.website=feat['properties'].get('website')
                properties.address_id=feat['properties'].get('address_id')
                properties.alt_name=feat['properties'].get('alt_name')
                properties.restriction=feat['properties'].get('restriction')

                # create display_point object if it exists in input
                display_point = None
                if 'display_point' in feat['properties'] and feat.get('properties').get('display_point'):
                    display_point = DisplayPoint()
                    # display_point.type=feat['properties']['display_point'].get('type')
                    display_point.coordinates=feat['properties']['display_point'].get('coordinates')

                if display_point:
                    properties.display_point=display_point

                # rest of feature keys mapping
                feature.id=feat['properties'].get('id')

            if properties:
                feature.properties = properties

            features.append(feature)

    venue = Venue()
    venue.type = venue_dict.get('type')
    venue.name = venue_dict.get('name')
    if features :
        venue.features = features

    return asdict(venue)


def convert_venue(inFilePath, outFilePath) :
    try:
        print("reading Venue input file ...")
        with open(inFilePath, "r") as in_venue_file:
            venue_dict_in = json.load(in_venue_file)
            print("Successfully read Venue input file!")
    except FileNotFoundError as e:
        print(f"Error : {e.strerror} : \"Input File '{e.filename}' does not exist. Please enter a valid file path/name.\"")

        raise SystemExit

    venue_imdf_dict = __map_venue(venue_dict_in)
    venue_imdf_json = json.dumps(venue_imdf_dict, indent=4)
    # print(venue_imdf_json)

    out_path_obj = Path(outFilePath)
    out_path_obj.resolve().parent.mkdir(parents=True, exist_ok = True)
    with out_path_obj.open(mode='w') as out_file:
        print("writing to Venue output file ...")
        out_file.write(venue_imdf_json)
    print("Successfully wrote Venue to output file!\n"+"-"*50)


def __main():
    args = sys.argv[1:]
    try:
        inFilePath = args[0]
        outFilePath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input file and Output file, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\n Venue Conversion started.")

    convert_venue(inFilePath, outFilePath)

if __name__ == "__main__":
    __main()