import sys
import json
from pathlib import Path
from dataclasses import asdict
from address.address import Address
from address.properties import Properties
from address.features import Features


def __map_address(address_dict: dict) -> dict:
    features = []
    if 'features' in address_dict:
        for feat in address_dict.get('features'):
            feature = Features(feature_type="address")

            feature.geometry = feat.get('geometry')

            # create properties object if it exists in input
            properties = None
            if 'properties' in feat and feat.get('properties'):
                properties = Properties()
                properties.address = feat['properties'].get('address')
                properties.unit = feat['properties'].get('unit')
                properties.locality = feat['properties'].get('locality')
                properties.province = feat['properties'].get('province')
                properties.country = feat['properties'].get('country')
                properties.postal_code = feat['properties'].get('postal_code')
                properties.postal_code_ext = feat['properties'].get(
                    'postal_code_ext')
                properties.postal_code_vanity = feat['properties'].get(
                    'postal_code_vanity')

                # rest of feature keys mapping
                feature.id = feat['properties'].get('id')

            if properties:
                feature.properties = properties

        features.append(feature)

    address = Address()
    address.type = address_dict.get('type')
    address.name = address_dict.get('name')
    if features:
        address.features = features

    return asdict(address)


def convert_address(inFilePath, outFilePath):
    try:
        print("reading Address input file ...")
        with open(inFilePath, "r") as in_address_file:
            address_dict_in = json.load(in_address_file)
            print("Successfully read Address input file!")
    except FileNotFoundError as e:
        print(
            f"Error : {e.strerror} : \"Input File '{e.filename}' does not exist. Please enter a valid file path/name.\"")

        raise SystemExit

    address_imdf_dict = __map_address(address_dict_in)
    address_imdf_json = json.dumps(address_imdf_dict, indent=4)
    # print(venue_imdf_json)

    out_path_obj = Path(outFilePath)
    out_path_obj.resolve().parent.mkdir(parents=True, exist_ok=True)
    with out_path_obj.open(mode='w') as out_file:
        print("writing to Address output file ...")
        out_file.write(address_imdf_json)
    print("Successfully wrote Address to output file!\n"+"-"*50)


def __main():
    args = sys.argv[1:]
    try:
        inFilePath = args[0]
        outFilePath = args[1]
    except IndexError:
        print(
            f"Expected 2 arguments : Input file and Output file, got {len(args)}. Please try again with 2 arguments.")
        raise SystemExit

    print("\nAddress Conversion started.")

    convert_address(inFilePath, outFilePath)


if __name__ == "__main__":
    __main()
