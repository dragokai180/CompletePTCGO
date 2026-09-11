from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="5e24c67b-9794-5204-9c52-b1ad50758ba7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesMorpeko.Name",
    display_name="Marnie's Morpeko",
    searchable_by=["Marnie's Morpeko", "Basic", "MarniesMorpeko"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=877,
    abilities=[
        Attack(
            title="Spiky Wheel",
            game_text="This attack does 40 more damage for each Darkness Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
