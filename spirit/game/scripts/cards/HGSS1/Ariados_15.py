from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ea3e5963-706b-55c8-86af-9c00680dd879',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name',
    display_name='Ariados',
    searchable_by=['Ariados', 'Stage 1', 'Ariados'],
    subtypes=['Stage 1'],
    collector_number=15,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name',
    family_id=167,
    abilities=[
        Attack(
            title='Leech Life',
            game_text='Remove from Ariados the number of damage counters equal to the damage you did to the Defending Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Poisonous Saliva',
            game_text='The Defending Pokémon is now Poisoned.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
