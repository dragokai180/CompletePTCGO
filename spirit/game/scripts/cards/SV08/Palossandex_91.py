from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="2b2c0a6d-a979-5cf0-9116-a66ecd75b23e",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palossandex.Name",
    display_name="Palossand ex",
    searchable_by=["Palossand ex", "Stage 1", "Tera", "ex", "Palossandex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=91,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    family_id=769,
    abilities=[
        Attack(
            title="Sand Tomb",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=standard_attack,
        ),
        Attack(
            title="Barite Jail",
            game_text="Put damage counters on each of your opponent's Benched Pokémon until its remaining HP is 100.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
