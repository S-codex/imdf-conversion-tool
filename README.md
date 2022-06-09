# IMDF Conversion Tool 0.0.1

## _Prerequisites_
 - Python >= 3.7

## _Usage Instructions_

1. Open command line(terminal) and navigate to the tool directory, or open the terminal at the tool directory location.
2. Run the tool script using following command :
    ```
    python imdf_tool.py <input geojson path+name> <output file path+name>
    ```

### Example commands (Windows)
1. When input and output are in the same directory -
    ```
    python imdf_tool.py venue_input.geojson tool_venue_output.geojson
    ```
2. Input and Output are placed elsewhere in the system -
    ```
    python imdf_tool.py C:\User\Desktop\venue_input.geojson C:\User\Desktop\tool_venue_output.geojson
    ```
    _For other systems - Linux/MacOS, use the corresponding system path format for input and output file paths_

## _Limitations / Considerations_
- As per v0.0.1, the tool expects the input structure of **coordinates** to be exactly a triple-nested list of coordinate pairs. (Refer to the sample input provided with the tool)
