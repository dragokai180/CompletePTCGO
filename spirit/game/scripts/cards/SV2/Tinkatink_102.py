from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d8edf5a1-62d8-511a-8724-3da55480f9e9',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name',
    display_name='Tinkatink',
    searchable_by=['Tinkatink', 'Basic', 'Tinkatink'],
    subtypes=['Basic'],
    collector_number=102,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=957,
    abilities=[
        Attack(
            title='Brutal Swing',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
