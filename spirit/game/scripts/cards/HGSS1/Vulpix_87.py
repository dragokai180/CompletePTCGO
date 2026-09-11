from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ac8d9442-6a42-553d-913a-fbefab72dc85',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name',
    display_name='Vulpix',
    searchable_by=['Vulpix', 'Basic', 'Vulpix'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=37,
    abilities=[
        Attack(
            title='Singe',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Burned.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ember',
            game_text='Flip a coin. If tails, discard a Fire Energy attached to Vulpix.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
