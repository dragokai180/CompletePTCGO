from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c872c30b-fb7d-536e-a64b-12878fc1668b',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name',
    display_name='Larvitar',
    searchable_by=['Larvitar', 'Basic', 'Larvitar'],
    subtypes=['Basic'],
    collector_number=110,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=246,
    abilities=[
        Attack(
            title='Double Stab',
            game_text='Flip 2 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
