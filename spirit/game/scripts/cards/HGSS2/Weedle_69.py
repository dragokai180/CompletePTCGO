from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c76b2e4f-62ef-5cce-9bc2-9e750e994dd3',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weedle.Name',
    display_name='Weedle',
    searchable_by=['Weedle', 'Basic', 'Weedle'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=13,
    abilities=[
        Attack(
            title='Speed Evolution',
            game_text='Search your deck for a card that evolves from Weedle and put it onto Weedle. (This counts as evolving Weedle.) Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sting',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
