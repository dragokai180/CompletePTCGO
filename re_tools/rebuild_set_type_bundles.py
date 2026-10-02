"""Rebuild a card set as small, independently validated type bundles."""

import argparse
import gc
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

import UnityPy

from re_tools import create_card_bundle
from spirit.server.bundle_variants import asset_number, card_partitions


def rebuild(set_code):
    root = Path(__file__).resolve().parents[1]
    cards_dir = root / "spirit" / "assets" / "cards" / set_code
    pips_dir = root / "spirit" / "assets" / "bundleCache" / "pips"
    cache_dir = root / "spirit" / "assets" / "bundleCache"
    template_dir = root / "spirit" / "templates" / "card_bundle"
    asset_map = json.loads((root / "spirit" / "server" / "asset_map.json").read_text())
    asset_names = asset_map[f"en_US_{set_code}"]
    partition = card_partitions()[set_code]
    images = {}
    for image in cards_dir.glob("*.png"):
        match = re.search(r"_(\d+)\.png$", image.name)
        if match:
            number = int(match.group(1))
            if number in images:
                raise ValueError(f"Duplicate image number {number}: {image}")
            images[number] = image

    groups = {}
    for asset_name in asset_names:
        number = asset_number(asset_name, set_code)
        if number is None or number not in partition:
            raise ValueError(f"Unclassified asset: {asset_name}")
        if "_energypip" in asset_name or "_toolpip" in asset_name:
            source = pips_dir / f"{set_code}_{int(number)}_{asset_name.split('_', 1)[1]}.png"
        else:
            source = images[number]
        if not source.is_file():
            raise FileNotFoundError(source)
        for kind in partition[number]:
            groups.setdefault(kind, {})[asset_name] = str(source)

    # Build outside the served cache, then publish each bundle only after all
    # of its objects and the expected card aliases have been read successfully.
    with tempfile.TemporaryDirectory(prefix=f"{set_code}_types_", dir=root / ".cache") as staging:
        create_card_bundle.OUTPUT_DIR = staging
        create_card_bundle.ASSET_MAP_PATH = str(Path(staging) / "no_asset_map.json")
        for kind, mapping in sorted(groups.items()):
            name = f"en_US_{set_code}_{kind}"
            create_card_bundle.create_card_set_bundle(
                mapping, str(template_dir), name)
            source = Path(staging) / name / "00000000000000000000000001000000" / "__data"
            if not source.is_file():
                raise RuntimeError(f"Bundle generation failed: {name}")
            env = UnityPy.load(source.read_bytes())
            aliases = {
                key for obj in env.objects if obj.type.name == "AssetBundle"
                for key, _ in obj.read().m_Container
            }
            missing = {f"{set_code}/{asset}" for asset in mapping} - aliases
            if missing:
                raise RuntimeError(f"Missing aliases in {name}: {sorted(missing)[:5]}")
            for obj in env.objects:
                obj.read()
            del env
            destination = cache_dir / name / "00000000000000000000000001000000" / "__data"
            destination.parent.mkdir(parents=True, exist_ok=True)
            with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as output:
                temporary = Path(output.name)
                with source.open("rb") as input_file:
                    shutil.copyfileobj(input_file, output)
            os.replace(temporary, destination)
            print(f"Published {name}: {len(mapping)} assets, {destination.stat().st_size} bytes", flush=True)
            gc.collect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set_code")
    rebuild(parser.parse_args().set_code)
