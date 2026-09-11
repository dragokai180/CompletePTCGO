from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a9ab6bff-18fd-59cb-8520-ccdb680cd187',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name',
    display_name='Feebas',
    searchable_by=['Feebas', 'Basic', 'Feebas'],
    subtypes=['Basic'],
    collector_number=26,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=349,
    abilities=[
        Attack(
            title='Splashing Dodge',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
