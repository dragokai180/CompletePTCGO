from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9ecb3c0f-77de-552b-9ead-69912893b831',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name',
    display_name='Feebas',
    searchable_by=['Feebas', 'Basic', 'Feebas'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=349,
    abilities=[
        Ability(
            title='Submerge',
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).",
            passive=standard_passive("As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's)."),
        ),
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
