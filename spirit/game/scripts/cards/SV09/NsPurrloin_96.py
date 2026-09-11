from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="dc126e08-e5cc-517a-82b6-e635af158f3e",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsPurrloin.Name",
    display_name="N's Purrloin",
    searchable_by=["N's Purrloin", "Basic", "NsPurrloin"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=509,
    abilities=[
        Attack(
            title="Thieving Swipe",
            game_text="Your opponent reveals their hand, and you choose a card you find there and put it on the bottom of their deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
