from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5165788f-e484-5a76-8255-6f4a09c7422c',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name',
    display_name='Solrock',
    searchable_by=['Solrock', 'Basic', 'Solrock'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=338,
    abilities=[
        Attack(
            title='Solar Generator',
            game_text='Search your deck for up to 2 Special Energy cards, reveal them, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Knock Away',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
