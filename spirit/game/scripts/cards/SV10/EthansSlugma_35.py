from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="71856159-40e5-5ae4-81e3-c3c5c99c4330",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSlugma.Name",
    display_name="Ethan's Slugma",
    searchable_by=["Ethan's Slugma", "Basic", "EthansSlugma"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=218,
    abilities=[
        Attack(
            title="Steady Firebreathing",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
    ],
)
