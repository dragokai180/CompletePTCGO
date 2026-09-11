from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e34c213-c43e-5a43-89c5-b31827579bbe',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Latios.Name',
    display_name='Latios',
    searchable_by=['Latios', 'Basic', 'Latios'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=381,
    abilities=[
        Attack(
            title='Supersonic Flight',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Psyburn',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
