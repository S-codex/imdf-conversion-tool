# IMDF Conversion Tool 1.0.0

## _Prerequisites_
 - Python >= 3.7

## _Usage Instructions_

1. Open command line(terminal) and navigate to the tool directory, or open the terminal at the tool directory location.
2. Run the tool script using following command :
    ```
    python imdf_tool.py <input geojson directpry path> <output directory path>
    ```

### Example commands (Windows)
1. When input and output are in the same directory as tool -
    ```
    python imdf_tool.py Input_Geojson Tool_Geojson
    ```
2. Input and Output are placed elsewhere in the system -
    ```
    python imdf_tool.py C:\User\Desktop\Input_Geojson C:\User\Desktop\Output_Geojson
    ```
    _For other systems - Linux/MacOS, use the corresponding system path format for input and output directory paths_

## _Limitations / Considerations_
- As per v1.0.0, the tool expects the input structure of **coordinates** in **venue** module to be exactly a triple-nested list of coordinate pairs.
