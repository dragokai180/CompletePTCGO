from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="31d206db-7d78-5114-a3f8-84605667c118",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorbex.Name",
    display_name="Voltorb ex",
    searchable_by=["Voltorb ex", "Basic", "ex", "Voltorbex"],
    subtypes=["Basic", "ex"],
    collector_number=58,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=100,
    abilities=[
        Attack(
            title="Hundred-Hitting Ball",
            game_text="Flip a coin until you get tails. This attack does 100 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
