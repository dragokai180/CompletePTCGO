from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a1301206-89f2-5bf1-bc77-1b8b4b15d88a',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeist.Name',
    display_name='Gourgeist',
    searchable_by=['Gourgeist', 'Stage 1', 'Gourgeist'],
    subtypes=['Stage 1'],
    collector_number=45,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name',
    family_id=710,
    abilities=[
        Ability(
            title='Gourgantic',
            game_text='If this Pokémon has any Grass Energy attached to it, its maximum HP is 200.',
            passive=standard_passive('If this Pokémon has any Grass Energy attached to it, its maximum HP is 200.'),
        ),
        Attack(
            title='Horror Note',
            game_text='This attack does 10 damage times the number of cards in your hand.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
