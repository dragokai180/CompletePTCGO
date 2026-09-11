from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f9913f1-2b63-5627-a570-13329a022941',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bonsly.Name',
    display_name='Bonsly',
    searchable_by=['Bonsly', 'Basic', 'Bonsly'],
    subtypes=['Basic'],
    collector_number=110,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=438,
    abilities=[
        Attack(
            title='Blubbering',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
