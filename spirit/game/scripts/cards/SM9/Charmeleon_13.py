from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4c741b58-8765-5a17-ab82-75ad60623cd5',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    display_name='Charmeleon',
    searchable_by=['Charmeleon', 'Stage 1', 'Charmeleon'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name',
    family_id=4,
    abilities=[
        Attack(
            title='Fire Fang',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
