from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ac127455-f08c-5c01-ad85-fd10c77a774a',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name',
    display_name='Eelektrik',
    searchable_by=['Eelektrik', 'Stage 1', 'Eelektrik'],
    subtypes=['Stage 1'],
    collector_number=63,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name',
    family_id=602,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Buzz Flip',
            game_text='Flip 4 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
