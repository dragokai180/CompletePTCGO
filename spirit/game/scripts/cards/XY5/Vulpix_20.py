from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='074c8611-bd70-56fe-87e4-53ed839a50ca',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name',
    display_name='Vulpix',
    searchable_by=['Vulpix', 'Basic', 'Vulpix'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=37,
    abilities=[
        Attack(
            title='Roar',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Gnaw',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)
