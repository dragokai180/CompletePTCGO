from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b347109c-2609-57be-af91-cb89f1386eb0',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name',
    display_name='Dartrix',
    searchable_by=['Dartrix', 'Stage 1', 'Dartrix'],
    subtypes=['Stage 1'],
    collector_number=19,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name',
    family_id=722,
    abilities=[
        Attack(
            title='Leafage',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title='Wing Flick',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
