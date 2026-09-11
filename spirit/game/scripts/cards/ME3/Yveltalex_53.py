from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="913b2cae-eeec-51e8-9afd-8fdd4f31e8f3",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltalex.Name",
    display_name="Yveltal ex",
    searchable_by=["Yveltal ex", "Basic", "ex", "Yveltalex"],
    subtypes=["Basic", "ex"],
    collector_number=53,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=717,
    abilities=[
        Attack(
            title="Soul Destroyer",
            game_text="Knock Out each of your opponent's Pokémon that has 50 HP or less remaining.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Dark Strike",
            game_text="During your next turn, this Pokémon can't use Dark Strike.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
