# Software Update System

A robust framework for performing non-disruptive software updates across interconnected processes in complex systems where continuous operation is critical.

## Overview

The Software Update System enables updating software components in a metrology and control system without interrupting hardware operations. Traditional update approaches require stopping all software processes (drivers) before patching, resulting in significant downtime due to complex initialization sequences. This system addresses this limitation by enabling targeted updates while keeping hardware-interfacing components operational.

## Key Applications

- Industrial Control Systems: Update supervisory control software without disrupting equipment operation
- Instrumentation Platforms: Patch measurement and metrology components while maintaining data collection
- Distributed Systems: Update selected components in a network of interconnected processes
- Critical Infrastructure: Apply software patches with minimal service interruption

## Features

- Selective Updates: Target specific software modules without shutting down the entire system
- Dependency Management: Handle dependencies between interconnected processes
- Update Validation: Verify update integrity before and after application
- Rollback Capability: Automatically restore previous versions if updates fail
- System Monitoring: Track system health metrics during the update process
- Package Management: Install, remove, and track software packages
- Inter-Process Communication: Coordinate updates across distributed components

## Technologies

- Python 3.6+: Core application language
- Flask: RESTful API for remote update management
- PyYAML: Configuration management
- Pytest: Comprehensive test framework
- Psutil: System resource monitoring
- Schedule: Task scheduling for automated updates
- Multiprocessing: Inter-process communication

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd software-update-system
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the installation script:
   ```
   ./scripts/install.sh    # For Linux/Mac
   ```
   Or on Windows:
   ```
   python scripts/install.py
   ```

## Usage

### Basic Update Process

To start the update process manually:
```
python src/main.py
```

### Scheduled Updates

Configure and run automated updates:
```
python scripts/update_scheduler.py
```

### Custom Update Configuration

1. Modify `config/system_config.yaml` to customize:
   - Update frequency
   - Rollback settings
   - Notification preferences
   - System monitoring parameters

2. Define process dependencies in the configuration to ensure proper update sequencing

## Configuration

Configuration files in the `config` directory control system behavior:

- `system_config.yaml`: Core update behavior and dependencies
- `logging_config.yaml`: Logging levels and destinations

## Testing

Unit tests ensure reliability of all system components:
```
python -m unittest discover -s tests
```

Or with pytest:
```
pytest tests/
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.