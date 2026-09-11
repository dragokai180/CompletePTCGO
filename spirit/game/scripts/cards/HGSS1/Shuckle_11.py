from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4f367e04-625f-552d-ac11-6833d39cdc56',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shuckle.Name',
    display_name='Shuckle',
    searchable_by=['Shuckle', 'Basic', 'Shuckle'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=213,
    abilities=[
        Ability(
            title='Shell Barricade',
            game_text="As long as Shuckle is on your Bench, prevent all damage done to Shuckle by attacks (both yours and your opponent's).",
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive("As long as Shuckle is on your Bench, prevent all damage done to Shuckle by attacks (both yours and your opponent's)."),
        ),
        Attack(
            title='Poison Jab',
            game_text='The Defending Pokémon is now Poisoned.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
