from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='87729a9b-eb42-5643-b391-17fbf52fcfb1',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name',
    display_name='Tandemaus',
    searchable_by=['Tandemaus', 'Basic', 'Tandemaus'],
    subtypes=['Basic'],
    collector_number=153,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=924,
    abilities=[
        Attack(
            title='Damage Rush',
            game_text='Flip a coin until you get tails. This attack does 10 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
