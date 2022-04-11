#!/usr/bin/python3
# -*- coding: utf-8 -*-

from classes.BlindageInterface import BlindageInterface
from classes.BlindageLoader import BlindageLoader
from classes.BlindageSelector import BlindageSelector
from classes.BlindageConfigurator import BlindageConfigurator
from classes.BlindageConfiguratorCache import BlindageConfiguratorCache
from classes.BlindageGenerator import BlindageGenerator
from classes.BlindageEncoder import BlindageEncoder
from classes.BlindageWriter import BlindageWriter
from classes.BlindageTipper import BlindageTipper


def main():
    print((
        "█▀▀▄ █░░ ░▀░ █▀▀▄ █▀▀▄ █▀▀█ █▀▀▀ █▀▀\n"
        "█▀▀▄ █░░ ▀█▀ █░░█ █░░█ █▄▄█ █░▀█ █▀▀\n"
        "▀▀▀░ ▀▀▀ ▀▀▀ ▀░░▀ ▀▀▀░ ▀░░▀ ▀▀▀▀ ▀▀▀\n"
        "use responsibly (͡° ͜ʖ ͡°)\n"
    ))

    BlindageInterface.print_good("Loading...")

    module_loader = BlindageLoader(BlindageInterface)
    modules = module_loader.load()

    selector = BlindageSelector(BlindageInterface)
    selected_modules = selector.start(modules)

    configurator_cache = BlindageConfiguratorCache(BlindageInterface)
    configurator = BlindageConfigurator(BlindageInterface, configurator_cache)
    configured_modules = configurator.start(selected_modules)

    generator = BlindageGenerator(BlindageInterface)
    script = generator.start(configured_modules)

    encoder = BlindageEncoder(BlindageInterface)
    encoded_script = encoder.start(script)

    writer = BlindageWriter(BlindageInterface)
    writer.start(encoded_script)

    tipper = BlindageTipper(BlindageInterface)
    tipper.start(configured_modules)

    BlindageInterface.print_good("All done")


if __name__ == "__main__":
    main()
