from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="af967b29-44a1-50af-96c4-4879fd2ed400",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizarex.Name",
    display_name="Cyclizar ex",
    searchable_by=["Cyclizar ex", "Basic", "Tera", "ex", "Cyclizarex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=159,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=967,
    abilities=[
        Attack(
            title="Break Through",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=standard_attack,
        ),
        Attack(
            title="Zircon Road",
            game_text="You may draw 5 cards.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1},
            damage=180,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
