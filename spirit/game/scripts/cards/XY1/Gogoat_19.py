from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8be74cba-f91a-57b2-a5d9-be9d45b43660',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gogoat.Name',
    display_name='Gogoat',
    searchable_by=['Gogoat', 'Stage 1', 'Gogoat'],
    subtypes=['Stage 1'],
    collector_number=19,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name',
    family_id=672,
    abilities=[
        Attack(
            title='Lead',
            game_text='Search your deck for up to 2 Supporter cards, reveal them, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Charge Dash',
            game_text='You may do 20 more damage. If you do, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
