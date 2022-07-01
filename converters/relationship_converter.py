import sys
from pathlib import Path
import json
from dataclasses import asdict
from relationship.feature_reference import FeatureReference
from relationship.relationship import Relationship
from relationship.properties import Properties
from relationship.geometry import Geometry
from relationship.features import Features


def __map_relationship(relationship_dict: dict) -> dict:
    features = []
    if 'features' in relationship_dict:
        for feat in relationship_dict.get('features'):
            feature = Features(feature_type="relationship")

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
                properties.direction = feat['properties'].get('direction')
                properties.hours = feat['properties'].get('hours')

                # create origin object if it exists in input
                origin = None
                if 'origin' in feat['properties'] and feat.get('properties').get('origin'):
                    origin = FeatureReference()
                    origin.feature_type = feat.get('properties').get(
                        'origin').get('feature_type')
                    origin.id = feat.get('properties').get(
                        'origin').get('id')
                properties.origin = origin

                # create destination object if it exists in input
                destination = None
                if 'destination' in feat['properties'] and feat.get('properties').get('destination'):
                    destination = FeatureReference()
                    destination.feature_type = feat.get('properties').get(
                        'destination').get('feature_type')
                    destination.id = feat.get('properties').get(
                        'destination').get('id')
                properties.destination = destination

                intermediary = None
                if 'intermediary' in feat["properties"] and feat.get('properties').get('intermediary'):
                    intermediaries = []
                    for in_interm in feat.get('properties').get('intermediary'):
                        out_interm = FeatureReference()
                        out_interm.id = in_interm.get('id')
                        out_interm.feature_type = in_interm.get('feature_type')

                        intermediaries.append(out_interm)

                    intermediary = intermediaries

                if intermediary:
                    properties.intermediary = intermediary

                # rest of feature keys mapping
                feature.id = feat['properties'].get('id')

            if properties:
                feature.properties = properties

            features.append(feature)

    relationship = Relationship()
    relationship.type = relationship_dict.get('type')
    relationship.name = relationship_dict.get('name')
    if features:
        relationship.features = features

    return asdict(relationship)


def convert_relationship(inFilePath, outFilePath):
    try:
        print("reading Relationship input file ...")
        with open(inFilePath, "r") as in_relationship_file:
            relationship_dict_in = json.load(in_relationship_file)
            print("Successfully read Relationship input file!")
    except FileNotFoundError as e:
        print(
            f"Error : {e.strerror} : \"Input File '{e.filename}' does not exist. Please enter a valid file path/name.\"")

        raise SystemExit

    relationship_imdf_dict = __map_relationship(relationship_dict_in)
    relationship_imdf_json = json.dumps(relationship_imdf_dict, indent=4)
    # print(relationship_imdf_json)

    out_path_obj = Path(outFilePath)
    out_path_obj.resolve().parent.mkdir(parents=True, exist_ok=True)
    with out_path_obj.open(mode='w') as out_file:
        print("writing to Relationship output file ...")
        out_file.write(relationship_imdf_json)
    print("Successfully wrote Relationship to output file!\n"+"-"*50)


def __main():
    args = sys.argv[1:]
    try:
        inFilePath = args[0]
        outFilePath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input file and Output file, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\n Relationship Conversion started.")

    convert_relationship(inFilePath, outFilePath)


if __name__ == "__main__":
    __main()
