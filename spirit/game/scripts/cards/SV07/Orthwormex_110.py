from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="a7af1863-a17d-5ce3-9aa6-dddf5037ba70",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orthwormex.Name",
    display_name="Orthworm ex",
    searchable_by=["Orthworm ex", "Basic", "ex", "Orthwormex"],
    subtypes=["Basic", "ex"],
    collector_number=110,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=968,
    abilities=[
        Ability(
            title="Pummeling Payback",
            game_text="If this Pokémon is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon for each Metal Energy attached to this Pokémon.",
            effect=standard_ability,
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
        ),
        Attack(
            title="Rock Tomb",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
