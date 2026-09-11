from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e0177405-3162-5737-962b-4528d1d0daa0',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name',
    display_name='Meowth',
    searchable_by=['Meowth', 'Basic', 'Meowth'],
    subtypes=['Basic'],
    collector_number=75,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=52,
    abilities=[
        Attack(
            title='Pay Day',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Dig Claws',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
