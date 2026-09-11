from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f6a82dde-5e18-52b7-85bb-cfcfe54b18e9',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meowstic.Name',
    display_name='Meowstic',
    searchable_by=['Meowstic', 'Stage 1', 'Meowstic'],
    subtypes=['Stage 1'],
    collector_number=60,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name',
    family_id=677,
    abilities=[
        Attack(
            title='Allure',
            game_text='Draw 3 cards.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hand Kinesis',
            game_text='This attack does 10 damage for each card in your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
