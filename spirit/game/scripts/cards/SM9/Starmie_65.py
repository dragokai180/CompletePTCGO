from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a5868f6-066e-5020-9c40-ebbb7e6303f1',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name',
    display_name='Starmie',
    searchable_by=['Starmie', 'Stage 1', 'Starmie'],
    subtypes=['Stage 1'],
    collector_number=65,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name',
    family_id=120,
    abilities=[
        Attack(
            title='Strange Wave',
            game_text='Search your deck for up to 3 in any combination of Water and Psychic Energy cards and attach them to 1 of your Benched Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
