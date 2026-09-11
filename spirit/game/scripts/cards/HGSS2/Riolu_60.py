from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='56b7ca6f-3105-5e30-82a9-6de90ef5196b',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    display_name='Riolu',
    searchable_by=['Riolu', 'Basic', 'Riolu'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=447,
    abilities=[
        Attack(
            title='Kick',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Double Chop',
            game_text='Flip 2 coins. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
