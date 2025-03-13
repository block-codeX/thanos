# Thanos - Python & JavaScript to Sui Move Transpiler

Thanos is a transpiler that converts Python and JavaScript code into Sui Move smart contracts. It allows developers to write smart contract logic using a familiar syntax while ensuring compatibility with Sui Move.

## Features
- Transpiles Python and JavaScript into Sui Move

- Provides a scaffold generator to initialize projects quickly

- AST-based parsing and IR conversion for accurate transpilation

- Supports Move-specific constructs through a custom DSL

- Integrated build and deployment with Sui CLI

## Installation
```sheel
# Clone the repository
git clone https://github.com/yourusername/thanos.git
cd thanos

# Install dependencies
pip install -r requirements.txt
```

## Usage
### 1. Generate a new project scaffold
```shell
python thanos.py init my_project
cd my_project
```

### 2. Write smart contract logic using the framework
Example in Python:
```shell
from thanos import move_module, move_function, u64

@move_module
class MyModule:
    @move_function
    def add(a: u64, b: u64) -> u64:
        return a + b
```

### 3. Transpile to Sui Move

```shell
python thanos.py transpile my_project/main.py -o output/
```

### 4. Build and deploy
```shell
sui move build
sui client publish
```

## Architecture Overview
1. Front-end Parser: Converts Python/JS code into an Abstract Syntax Tree (AST).

2. Intermediate Representation (IR) Generator: Transforms AST into an intermediate representation compatible with Move.

3. Move Code Generator: Generates Sui Move code from IR.

4. Build & Deployment Pipeline: Integrates with the Sui CLI for compiling and deploying contracts.

## What Developers Need to Learn

- Python & JavaScript: For writing smart contract logic.

- Sui Move: Understanding Move's syntax and transaction model.

- AST & Transpilers: How code is parsed and transformed.

- Intermediate Representation (IR): Bridge between source and target languages.

- Sui CLI & Smart Contract Deployment: Building and publishing Move contracts.

## Contributing
We welcome contributions! Please fork the repo and submit a pull request.

## License
MIT License
