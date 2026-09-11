from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='57a8e4d6-4701-5701-9d87-0cdee26ef7d9',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name',
    display_name='Tadbulb',
    searchable_by=['Tadbulb', 'Basic', 'Tadbulb'],
    subtypes=['Basic'],
    collector_number=74,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=938,
    abilities=[
        Attack(
            title='Energize',
            game_text='Attach a Basic Lightning Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Lightning Ball',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
