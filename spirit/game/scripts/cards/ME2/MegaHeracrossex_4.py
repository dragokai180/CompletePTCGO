from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="f8c71aa2-458a-5b14-8ba2-987f995f4368",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaHeracrossex.Name",
    display_name="Mega Heracross ex",
    searchable_by=["Mega Heracross ex", "Basic", "MEGA", "ex", "SV_Mega", "MegaHeracrossex"],
    subtypes=["Basic", "MEGA", "ex", "SV_Mega"],
    collector_number=4,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=214,
    abilities=[
        Attack(
            title="Juggernaut Horn",
            game_text="If this Pokémon was damaged by an attack during your opponent's last turn, this attack does that much more damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
        Attack(
            title="Mountain Ramming",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.GRASS: 3},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
