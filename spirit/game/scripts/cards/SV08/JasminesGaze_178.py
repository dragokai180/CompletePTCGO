from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="1ff40e39-6d3a-5316-83ff-814875b5e872",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JasminesGaze.Name",
    display_name="Jasmine's Gaze",
    searchable_by=["Jasmine's Gaze", "Supporter", "JasminesGaze"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("During your opponent's next turn, all of your Pokémon take 30 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance). (This includes new Pokémon that come into play.)"),
)
