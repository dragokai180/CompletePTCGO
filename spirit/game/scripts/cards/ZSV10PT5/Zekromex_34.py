from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="bee5d1d1-ab86-5864-a1a1-16b5cc14de72",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekromex.Name",
    display_name="Zekrom ex",
    searchable_by=["Zekrom ex", "Basic", "ex", "Zekromex"],
    subtypes=["Basic", "ex"],
    collector_number=34,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=644,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Voltage Burst",
            game_text="This attack does 50 more damage for each Prize card your opponent has taken. This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
