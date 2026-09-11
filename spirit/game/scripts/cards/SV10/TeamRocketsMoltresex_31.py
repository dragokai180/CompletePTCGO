from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="ba921fb0-2372-5407-aaca-24b977d59650",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMoltresex.Name",
    display_name="Team Rocket's Moltres ex",
    searchable_by=["Team Rocket's Moltres ex", "Basic", "ex", "TeamRocketsMoltresex"],
    subtypes=["Basic", "ex"],
    collector_number=31,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=146,
    abilities=[
        Attack(
            title="Flame Screen",
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=standard_attack,
        ),
        Attack(
            title="Evil Incineration",
            game_text="Discard a Team Rocket's Energy from this Pokémon. If you do, discard your opponent's Active Pokémon and all attached cards.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
