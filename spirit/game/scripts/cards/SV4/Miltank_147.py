from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e3ac78a2-b8e4-5769-9f27-7fcfcca9a697',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name',
    display_name='Miltank',
    searchable_by=['Miltank', 'Basic', 'Miltank'],
    subtypes=['Basic'],
    collector_number=147,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=241,
    abilities=[
        Attack(
            title='Lively Tackle',
            game_text='If this Pokémon was healed during this turn, this attack does 90 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
