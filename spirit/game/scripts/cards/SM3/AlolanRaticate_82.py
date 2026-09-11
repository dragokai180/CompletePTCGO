from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e13f7ae3-bc8e-57d5-94fa-2d77a34a8cc7',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRaticate.Name',
    display_name='Alolan Raticate',
    searchable_by=['Alolan Raticate', 'Stage 1', 'AlolanRaticate'],
    subtypes=['Stage 1'],
    collector_number=82,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanRattata.Name',
    family_id=19,
    abilities=[
        Attack(
            title='Enhanced Fang',
            game_text='If this Pokémon has a Pokémon Tool card attached to it, this attack does 50 more damage.',
            cost={},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Hyper Fang',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
