from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2abb6fda-aa57-5fd1-875f-805bf2824df7',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    display_name='Charmeleon',
    searchable_by=['Charmeleon', 'Stage 1', 'Charmeleon'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code='SV3',
    regulation_mark='G',
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
            title='Heat Tackle',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.FIRE: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
