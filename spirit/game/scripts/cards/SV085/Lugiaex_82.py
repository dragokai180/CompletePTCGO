from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="bcefaffa-a561-50f1-9ed9-0897db73dbee",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugiaex.Name",
    display_name="Lugia ex",
    searchable_by=["Lugia ex", "Basic", "ex", "Lugiaex"],
    subtypes=["Basic", "ex"],
    collector_number=82,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=249,
    abilities=[
        Attack(
            title="Hyper Whirlpool",
            game_text="Flip a coin until you get tails. For each heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
