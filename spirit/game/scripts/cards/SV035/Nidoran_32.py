from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fc054abf-fd69-5833-b964-0b8a58eda5fc',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    display_name='Nidoran ♂',
    searchable_by=['Nidoran ♂', 'Basic', 'Nidoran'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=32,
    abilities=[
        Attack(
            title='Horn Attack',
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)
