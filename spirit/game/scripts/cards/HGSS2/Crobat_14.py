from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6368e3a2-ce5f-59fc-8620-31658eeb3196',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name',
    display_name='Crobat',
    searchable_by=['Crobat', 'Stage 2', 'Crobat'],
    subtypes=['Stage 2'],
    collector_number=14,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Golbat.Name',
    family_id=41,
    abilities=[
        Attack(
            title='Supersonic',
            game_text='The Defending Pokémon is now Confused.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Hurricane Wing',
            game_text='Flip 4 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
