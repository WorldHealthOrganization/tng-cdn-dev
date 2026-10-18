import json
import sys
from jsonschema import validate, ValidationError
from jsonschema.exceptions import best_match

def validate_json_with_file(data_filepath, schema_filepath):
    """
    Validates a JSON data file against a JSON schema file.

    Args:
        data_filepath (str): The path to the JSON data file.
        schema_filepath (str): The path to the JSON schema file.
    """
    try:
        with open(data_filepath, 'r') as data_file:
            json_data = json.load(data_file)

        with open(schema_filepath, 'r') as schema_file:
            json_schema = json.load(schema_file)

        validate(instance=json_data, schema=json_schema)
        print(f" Validation successful: '{data_filepath}' is valid against '{schema_filepath}'.")

    except FileNotFoundError:
        print(" Error: One or both of the specified files were not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f" Error: Invalid JSON format - {str(e)}")
        sys.exit(1)
    except ValidationError as e:
        print(f" Validation failed: '{data_filepath}' is invalid against '{schema_filepath}'.")

        error = best_match([e])
        path = ".".join([str(p) for p in error.path])
        if path:
            path = f" ➤ Field: `{path}`"
        else:
            path = ""

        if error.validator == "required":
            missing_field = error.message.split("'")[1]
            print(f" Missing required field{path}: `{missing_field}` is required.")
        elif error.validator == "type":
            expected_type = error.validator_value
            actual_type = type(error.instance).__name__
            print(f" Type mismatch{path}: Expected `{expected_type}`, but got `{actual_type}`.")
        elif error.validator == "pattern":
            print(f" Pattern mismatch{path}: Value does not match required pattern `{error.validator_value}`.")
        elif error.validator == "enum":
            print(f" Invalid value{path}: Must be one of {error.validator_value}.")
        else:
            print(f" Validation error{path}: {error.message}")
        sys.exit(1)

    except Exception as e:
        print(f" An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python did-json-schema-validation.py <data_file.json> <schema_file.json>")
        print("Example: python did-json-schema-validation.py did-trustlist.json did-trustlist-schema.json")
        sys.exit(1)

    data_file = sys.argv[1]
    schema_file = sys.argv[2]

    validate_json_with_file(data_file, schema_file)
