# Habit Tracker with Pixe.la

## Overview

This Python script interacts with the [Pixe.la API](https://docs.pixe.la/) to create a Pixe.la user, graph, and create/update/delete pixels from a graph. The Pixe.la service allows you to visually track and maintain records for various activities.

## Prerequisites

Make sure you have the following installed:

- Python (version 3.x)
- Required Python packages: `requests`. You can install it using the following command:

```bash
pip install requests
```

## Configuration

Before running the script, read the following documentation: [How to Use](https://pixe.la/#section-howtouse). Then Uncomment the relevant sections based on your requirements. Sections included are creating a user, create a graph, post a pixel for the current date or a specified date, update a pixel or to delete a pixel. 

Upon using the applicable sections, you can update the following variables in the script for ease of use:

- `USERNAME`: Your Pixe.la username.
- `TOKEN`: Your Pixe.la user token.
- `GRAPH_ID`: The ID of the graph on which you want to track pixels.
- `PROMPT`: The prompt corresponding to the measurement you want to track (e.g., "How many hours did you code today?").

## Usage

1. Clone the repository:

```
copy/download main.py to your project directory
```

2. Navigate to the project directory:

```
cd <project directory>
```

3. Edit the script and set the required configuration variables.

4. Run the script:

```bash
python mainy.py
```

Feel free to customize the script further based on your tracking needs.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ashjorda/100-Days-Of-Code/blob/master/LICENSE) file for details.