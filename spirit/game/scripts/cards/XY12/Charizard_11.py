from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b848637c-2a52-5a03-8275-f2dd0638807e',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name',
    display_name='Charizard',
    searchable_by=['Charizard', 'Stage 2', 'Charizard'],
    subtypes=['Stage 2'],
    collector_number=11,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    family_id=4,
    abilities=[
        Ability(
            title='Energy Burn',
            game_text='All Energy attached to this Pokémon are Fire Energy instead of their usual type.',
            passive=standard_passive('All Energy attached to this Pokémon are Fire Energy instead of their usual type.'),
        ),
        Attack(
            title='Fire Spin',
            game_text='Discard 3 Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 4},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
