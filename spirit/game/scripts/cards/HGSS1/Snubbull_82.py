from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3ac8c84-98b3-51bb-9457-1342119c4efc',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name',
    display_name='Snubbull',
    searchable_by=['Snubbull', 'Basic', 'Snubbull'],
    subtypes=['Basic'],
    collector_number=82,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=209,
    abilities=[
        Attack(
            title='Roar',
            game_text='Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
