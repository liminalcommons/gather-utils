# Portal Explorer Documentation

Welcome to the Portal Explorer documentation. This documentation provides comprehensive information about the Portal Explorer tool, which allows you to explore and analyze portals in Gather.town spaces.

## Table of Contents

- [User Guide](user_guide/index.md): Comprehensive guide for end users
- [API Reference](api/index.md): Technical documentation for developers
- [CLI Reference](cli/index.md): Detailed command-line interface documentation
- [Tutorials](tutorials/getting_started.md): Step-by-step guides for common tasks

## Quick Start

### Installation

```bash
pip install portal-explorer
```

### Configuration

Set environment variables:

```bash
export GATHER_API_KEY=your_api_key
export GATHER_SPACE_ID=your_space_id
```

Or create a configuration file at `~/.portal-explorer/config.ini`:

```ini
[gather]
api_key = your_api_key
space_id = your_space_id
```

### Basic Usage

List all maps in your Gather.town space:

```bash
gather-explorer list-maps
```

Explore portals in a specific map:

```bash
gather-explorer explore --map-id <map_id>
```

Explore portals across all maps:

```bash
gather-explorer explore --all-maps
```

## About Portal Explorer

Portal Explorer is a tool for exploring and analyzing portals in Gather.town spaces. It allows you to:

- List all maps in a Gather.town space
- Analyze portals in specific maps
- Analyze portals across all maps
- Visualize connections between maps
- Export portal information in various formats

## Contributing

Contributions to Portal Explorer are welcome! Please see the [GitHub repository](https://github.com/liminalcommons/gather-utils) for more information.

## License

Portal Explorer is licensed under the MIT License. See the [LICENSE](https://github.com/liminalcommons/gather-utils/blob/main/LICENSE) file for details.

---

This documentation was generated for Portal Explorer version 1.0.0. For the latest documentation, please visit the [project repository](https://github.com/liminalcommons/gather-utils).
