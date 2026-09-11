from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='85255362-5cac-58ce-ab08-53df0650013d',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name',
    display_name='Celebi ◇',
    searchable_by=['Celebi ◇', 'Basic', 'Prism Star', 'Celebi'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=19,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=251,
    abilities=[
        Attack(
            title='Time Distortion',
            game_text='Devolve any number of your Benched Pokémon as many times as you like. Put each Evolution card removed this way into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Leech Seed',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
