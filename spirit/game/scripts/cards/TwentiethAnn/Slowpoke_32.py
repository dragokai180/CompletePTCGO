from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='39c432ae-497f-5878-a493-bffedc5920b2',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    display_name='Slowpoke',
    searchable_by=['Slowpoke', 'Basic', 'Slowpoke'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=79,
    abilities=[
        Attack(
            title='Spacing Out',
            game_text='Flip a coin. If heads, heal 10 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Scavenge',
            game_text='Discard a Psychic Energy attached to this Pokémon. If you do, put an Item card from your discard pile into your hand.',
            cost={PokemonTypes.PSYCHIC: 2},
            effect=standard_attack,
        ),
    ],
)
