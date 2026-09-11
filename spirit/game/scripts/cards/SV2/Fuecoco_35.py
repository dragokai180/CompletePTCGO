from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='31c8b75a-e3e8-581f-b563-2e9498fbcc4a',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fuecoco.Name',
    display_name='Fuecoco',
    searchable_by=['Fuecoco', 'Basic', 'Fuecoco'],
    subtypes=['Basic'],
    collector_number=35,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=909,
    abilities=[
        Attack(
            title='Spacing Out',
            game_text='Flip a coin. If heads, heal 30 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
