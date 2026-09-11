from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a88d7ae9-23e4-5653-91c6-f82de1846696',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name',
    display_name='Wobbuffet',
    searchable_by=['Wobbuffet', 'Basic', 'Wobbuffet'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=202,
    abilities=[
        Attack(
            title='Double Return',
            game_text='Flip a coin. If heads, this attack does 20 damage times the number of damage counters on Wobbuffet.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
