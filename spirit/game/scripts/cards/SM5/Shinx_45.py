from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ac25c3e2-e256-5137-9895-6a7019a514f7',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name',
    display_name='Shinx',
    searchable_by=['Shinx', 'Basic', 'Shinx'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=403,
    abilities=[
        Ability(
            title='Evolutionary Advantage',
            game_text='If you go second, this Pokémon can evolve during your first turn.',
            passive=standard_passive('If you go second, this Pokémon can evolve during your first turn.'),
        ),
        Attack(
            title='Static Shock',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
    ],
)
