from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6d7e8dd2-fef5-54ed-8ef9-e65e8a9e2c7c",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaZeraoraex.Name",
    display_name="Mega Zeraora ex",
    searchable_by=["Mega Zeraora ex", "Basic", "MEGA", "ex", "SV_Mega", "MegaZeraoraex"],
    subtypes=["Basic", "MEGA", "ex", "SV_Mega"],
    collector_number=27,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=807,
    abilities=[
        Attack(
            title="Thunderous Fist",
            game_text="This attack does 60 damage for each Lightning Energy attached to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            damage_operator="x",
            effect=standard_attack,
        ),
        Attack(
            title="Zepto Turn",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
