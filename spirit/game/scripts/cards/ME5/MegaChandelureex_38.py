from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="11637729-6873-5d82-b221-7441bbd6da92",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaChandelureex.Name",
    display_name="Mega Chandelure ex",
    searchable_by=["Mega Chandelure ex", "Stage 2", "MEGA", "ex", "SV_Mega", "MegaChandelureex"],
    subtypes=["Stage 2", "MEGA", "ex", "SV_Mega"],
    collector_number=38,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Binding Flame",
            game_text="Your opponent's Active Pokémon's Retreat Cost is Colorless more.",
            passive=standard_passive("Your opponent's Active Pokémon's Retreat Cost is Colorless more."),
        ),
        Attack(
            title="Phantom Maze",
            game_text="This attack does 50 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
