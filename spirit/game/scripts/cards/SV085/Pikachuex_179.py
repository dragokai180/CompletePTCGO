from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.card_effects.pokemon import TeraRulePassive


card = PokemonCardDef(
    guid="f417ff7c-4702-5f32-964e-5aa89b38fdb1",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name",
    display_name="Pikachu ex",
    searchable_by=["Pikachu ex", "Basic", "Tera", "ex", "Pikachuex"],
    subtypes=["Basic", "Tera", "ex"],
    collector_number=179,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareRainbow,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Ability(
            title="Resolute Heart",
            game_text="If this Pokémon has full HP and would be Knocked Out by damage from an attack, it is not Knocked Out, and its remaining HP becomes 10.",
            passive=standard_passive("If this Pokémon has full HP and would be Knocked Out by damage from an attack, it is not Knocked Out, and its remaining HP becomes 10."),
        ),
        Attack(
            title="Topaz Bolt",
            game_text="Discard 3 Energy from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.METAL: 1},
            damage=300,
            effect=standard_attack,
        ),
    ],
    passive=TeraRulePassive(),
)
