from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a4ffa291-0603-5914-9585-9c0c3bd3b567',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name',
    display_name='Spearow',
    searchable_by=['Spearow', 'Basic', 'Spearow'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=21,
    abilities=[
        Attack(
            title='Whirlwind',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
