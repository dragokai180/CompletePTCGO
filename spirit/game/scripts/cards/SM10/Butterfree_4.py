from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a37d3dbb-9b64-5730-b815-4e50e972bc96',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name',
    display_name='Butterfree',
    searchable_by=['Butterfree', 'Stage 2', 'Butterfree'],
    subtypes=['Stage 2'],
    collector_number=4,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name',
    family_id=10,
    abilities=[
        Attack(
            title='Triple Charge',
            game_text='Search your deck for up to 3 basic Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Solar Beam',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
