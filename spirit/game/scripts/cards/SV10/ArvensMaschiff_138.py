from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="cd966024-0b69-5ae5-9b7e-28dde3c66023",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensMaschiff.Name",
    display_name="Arven's Maschiff",
    searchable_by=["Arven's Maschiff", "Basic", "ArvensMaschiff"],
    subtypes=["Basic"],
    collector_number=138,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=942,
    abilities=[
        Attack(
            title="Stampede",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Confront",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
