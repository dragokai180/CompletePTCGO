# spirit/assets/cards
THE STRUCTURE OF THIS FOLDER MUST MATCH THAT OF game/scripts

The cards texture rely on these png files being in the same order and name as the scripts!

## Reprints (same card, different art / collector number)

Keep the full mechanics in one script (e.g. `IronLeavesex_25.py`). For alternate
printings, add matching PNGs plus a thin stub that calls `reprint(...)`:

```python
from spirit.game.attributes import Rarities
from spirit.game.data_utils import reprint, sibling_card

card = reprint(
    sibling_card(__file__, "IronLeavesex_25.py"),
    collector_number=186,
    rarity=Rarities.RareUltra,
)
```

Stub basename must match the PNG (`IronLeavesex_186.py` ↔ `IronLeavesex_186.png`).
