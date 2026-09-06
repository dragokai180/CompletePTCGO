from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import full_effect_shield_passive

card = PokemonCardDef(
    guid="9ba263d1-69c4-50b8-acfd-3670495bf880",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name",
    display_name="Shuppet",
    searchable_by=["Shuppet","Basic","Shuppet"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    family_id=353,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Ability(
            title="Hide 'n' Sneak",
            game_text="Prevent all effects of your opponent's Pokémon's attacks and Abilities done to this Pokémon. (Damage is not an effect.)",
            passive=full_effect_shield_passive(),
        ),
        Attack(
            title="Hang Down",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
