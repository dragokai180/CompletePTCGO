from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="c6c99f38-9d61-598d-ad56-f08412c97214",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansCyndaquil.Name",
    display_name="Ethan's Cyndaquil",
    searchable_by=["Ethan's Cyndaquil", "Basic", "EthansCyndaquil"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=155,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
