from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="9ef3635d-287a-5531-acd0-b3dac0df5014",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronBoulderex.Name",
    display_name="Iron Boulder ex",
    searchable_by=["Iron Boulder ex", "Basic", "ex", "Future", "IronBoulderex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=99,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=1022,
    abilities=[
        Attack(
            title="Repulsor Axe",
            game_text="During your opponent's next turn, if this Pokémon is damaged by an attack (even if it is Knocked Out), put 8 damage counters on the Attacking Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title="Power Stomp",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
