from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='19231a48-b1f9-581a-9b9a-a08abffa5b63',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slowbro.Name',
    display_name='Slowbro',
    searchable_by=['Slowbro', 'Stage 1', 'Slowbro'],
    subtypes=['Stage 1'],
    collector_number=38,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name',
    family_id=79,
    abilities=[
        Attack(
            title='Full-Belly Refresh',
            game_text='Remove all Special Conditions and 3 damage counters from Slowbro.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Startling Trip',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Confused. If tails, Slowbro is now Confused.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
