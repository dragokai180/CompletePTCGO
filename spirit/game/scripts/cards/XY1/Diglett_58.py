from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='69167ea7-b5cc-5c28-8809-c8b1e50242f5',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Diglett.Name',
    display_name='Diglett',
    searchable_by=['Diglett', 'Basic', 'Diglett'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=50,
    abilities=[
        Attack(
            title='Mine',
            game_text="Look at the top card of your opponent's deck. Then, you may have your opponent shuffle his or her deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mud-Slap',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
