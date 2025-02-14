#!/Users/carolinagiovagnoli/Documents/GitHub/maldovan-garamond/env/bin/python3.9
"""
gftools fix-font

Update a font so it conforms to the Google Fonts specification
https://github.com/googlefonts/gf-docs/tree/main/Spec

Usage:

gftools fix-font font.ttf

# Fix font issues that should be fixed in the source files
gftools fix-font font.ttf --include-source-fixes
"""
import argparse
import logging
from fontTools.ttLib import TTFont
from gftools.fix import *


log = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("font", help="Path to font")
    parser.add_argument("-o", "--out", help="Output path for fixed font")
    parser.add_argument(
        "--include-source-fixes",
        action="store_true",
        help="Fix font issues that should be fixed in the source files.",
    )
    args = parser.parse_args()

    font = TTFont(args.font)

    fix_font(font, args.include_source_fixes)

    if args.out:
        font.save(args.out)
    else:
        font.save(font.reader.file.name + ".fix")


if __name__ == "__main__":
    main()
