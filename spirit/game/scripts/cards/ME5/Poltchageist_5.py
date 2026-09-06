from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.card_effects.passives_common import full_effect_shield_passive

card = PokemonCardDef(
    guid="f45e7725-690a-576c-a33e-b86a99f4f743",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    display_name="Poltchageist",
    searchable_by=["Poltchageist","Basic","Poltchageist"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    family_id=1012,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Ability(
            title="Hide 'n' Sneak",
            game_text="Prevent all effects of your opponent's Pokémon's attacks and Abilities done to this Pokémon. (Damage is not an effect.)",
            passive=full_effect_shield_passive(),
        ),
        Attack(
            title="Furtive Drop",
            game_text="Place 1 damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=place_counters(1, "opponent_active"),
        ),
    ],
)
