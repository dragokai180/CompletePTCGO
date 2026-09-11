from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='185c445e-6ce1-598b-8462-4880cbc71da0',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    display_name='Slowpoke',
    searchable_by=['Slowpoke', 'Basic', 'Slowpoke'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=79,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Whimsy Tackle',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
