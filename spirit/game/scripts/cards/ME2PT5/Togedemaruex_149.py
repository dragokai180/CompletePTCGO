from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="59854994-7efb-590d-a34e-d9762335d4eb",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaruex.Name",
    display_name="Togedemaru ex",
    searchable_by=["Togedemaru ex", "Basic", "ex", "Togedemaruex"],
    subtypes=["Basic", "ex"],
    collector_number=149,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=777,
    abilities=[
        Attack(
            title="Stun Needle",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title="Spiky Rolling",
            game_text="If this Pokémon used Spiky Rolling during your last turn, this attack does 80 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
