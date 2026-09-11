from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ea800e9d-5341-5c60-ac28-88fcd6205c3e',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name',
    display_name='Nacli',
    searchable_by=['Nacli', 'Basic', 'Nacli'],
    subtypes=['Basic'],
    collector_number=121,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=932,
    abilities=[
        Attack(
            title='Salt Coating',
            game_text='Heal 20 damage from 1 of your Pokémon.',
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
