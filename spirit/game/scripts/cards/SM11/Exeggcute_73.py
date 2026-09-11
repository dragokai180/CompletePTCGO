from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b024ce01-5aae-53ca-91c3-c9136f034c1b',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    display_name='Exeggcute',
    searchable_by=['Exeggcute', 'Basic', 'Exeggcute'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=102,
    abilities=[
        Attack(
            title='Leech Seed',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
