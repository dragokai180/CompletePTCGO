from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cecbf94a-8415-5387-8b1d-69f0d3c236f5',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name',
    display_name='Shinx',
    searchable_by=['Shinx', 'Basic', 'Shinx'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=403,
    abilities=[
        Attack(
            title='Wild Kick',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
