from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6c5c0777-be36-56c1-905f-e6da60a2657d',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    display_name='Marill',
    searchable_by=['Marill', 'Basic', 'Marill'],
    subtypes=['Basic'],
    collector_number=34,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=183,
    abilities=[
        Attack(
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rollout',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
