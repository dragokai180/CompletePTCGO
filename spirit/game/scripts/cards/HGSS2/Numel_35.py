from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d6935d6-660d-5e2d-be20-516fb10c6dfa',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name',
    display_name='Numel',
    searchable_by=['Numel', 'Basic', 'Numel'],
    subtypes=['Basic'],
    collector_number=35,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=322,
    abilities=[
        Attack(
            title='Flare Bonus',
            game_text='Discard a Fire Energy card from your hand. Then, draw 3 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
