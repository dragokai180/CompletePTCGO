from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e78f4e19-cf3e-5930-a33f-488d8b5c7673',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name',
    display_name='Jolteon',
    searchable_by=['Jolteon', 'Stage 1', 'Jolteon'],
    subtypes=['Stage 1'],
    collector_number=26,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Ability(
            title='Electric Effect',
            game_text='Each of your Stage 1 Pokémon in play is now a Lightning Pokémon in addition to its existing types.',
            passive=standard_passive('Each of your Stage 1 Pokémon in play is now a Lightning Pokémon in addition to its existing types.'),
        ),
        Attack(
            title='Thunder Blast',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
