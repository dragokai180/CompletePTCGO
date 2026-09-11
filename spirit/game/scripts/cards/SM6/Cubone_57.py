from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5b2c19f5-54af-5b72-95b2-f409fd1f5b1c',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    display_name='Cubone',
    searchable_by=['Cubone', 'Basic', 'Cubone'],
    subtypes=['Basic'],
    collector_number=57,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=104,
    abilities=[
        Attack(
            title='Burdensome Bone',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
