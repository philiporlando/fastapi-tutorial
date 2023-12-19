# FastAPI Tutorial Project

## Overview

This repository contains my project files and notes while I follow along with the FastAPI tutorials. [FastAPI](https://fastapi.tiangolo.com/) is a modern, fast web framework for building APIs with Python based on standard Python type hints.

## Project Structure

- `chapters/`: Contains examples FastAPI applications that correspond to each chapter of the [tutorial](https://fastapi.tiangolo.com/tutorial/).

## Getting Started

### Prerequisites

- Python 3.7+
- [Poetry](https://python-poetry.org/) for dependency management

### Installation

1. Clone the repository:

   ```bash
   git clone [your-repository-url]
   cd [your-repository-name]
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

### Running the Examples

To run an example FastAPI application:

```bash
poetry run uvicorn examples.first_steps:app --reload
```

This command will start the Uvicorn server with auto-reload enabled.

## Contributing

Feel free to fork this repository and submit pull requests. You can also open issues for any bugs you find or features you think would be beneficial.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

- FastAPI [official documentation](https://fastapi.tiangolo.com/)
- Creator of FastAPI, Sebastián Ramírez

