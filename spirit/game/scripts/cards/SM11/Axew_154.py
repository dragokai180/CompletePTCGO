from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='72fe3440-9ab2-5893-9384-16f1f2624442',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name',
    display_name='Axew',
    searchable_by=['Axew', 'Basic', 'Axew'],
    subtypes=['Basic'],
    collector_number=154,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=610,
    abilities=[
        Ability(
            title='Unnerve',
            game_text='Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pokémon.',
            passive=standard_passive('Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pokémon.'),
        ),
        Attack(
            title='Gnaw',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.METAL: 1},
            damage=20,
        ),
    ],
)
