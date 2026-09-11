from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='10c2faba-4161-532f-addc-51158dc18569',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name',
    display_name='Chansey',
    searchable_by=['Chansey', 'Basic', 'Chansey'],
    subtypes=['Basic'],
    collector_number=144,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=113,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
        Attack(
            title='Egg Rolling',
            game_text='Flip a coin until you get tails. This attack does 60 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
