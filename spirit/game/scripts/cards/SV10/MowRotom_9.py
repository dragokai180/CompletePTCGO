from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="ae260771-d991-5440-a484-40af7a9eda92",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MowRotom.Name",
    display_name="Mow Rotom",
    searchable_by=["Mow Rotom", "Basic", "MowRotom"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=479,
    abilities=[
        Attack(
            title="Trimming Mower",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title="Gadget Show",
            game_text="This attack does 30 damage for each Pokémon Tool attached to all of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=standard_attack,
        ),
    ],
)
