from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7808dd74-c911-5fa4-a3be-e7aa02561547',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name',
    display_name='Makuhita',
    searchable_by=['Makuhita', 'Basic', 'Makuhita'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=296,
    abilities=[
        Attack(
            title='Slap Down',
            game_text='Flip 2 coins. This attack does 20 damage plus 10 more damage for each heads.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Slap Push',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
