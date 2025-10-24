# pack-tool

A simple tool for applying customizations to resource packs.

> Note: this tool is exclusively tested on Linux.(it should run on most Un*x-like systems as well)

## Depencencies

### Optional

- [McAssetExtractor](https://github.com/rmheuer/McAssetExtractor) - for downloading Minecraft assets

### Most of these are optional, install what you need
- [SoX](https://sourceforge.net/projects/sox/) - sound processing
- [ImageMagick](https://imagemagick.org) - image processing
- [oxipng](https://github.com/oxipng/oxipng) - png optimization(you probably won't need this)
- [OptiVorbis](https://github.com/OptiVorbis/OptiVorbis) - .ogg optimization(not needed unless you really want to)

### Required
- `python`
- `python-pyyaml` or PyPi package `pyyaml`

## Usage

- Configure your settings in the [configuration.yaml](./configuration.yaml) file.
- Run the script, if it fails, read your configuration.yml again or file an issue
