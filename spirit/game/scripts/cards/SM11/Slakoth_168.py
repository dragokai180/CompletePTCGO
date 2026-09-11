from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0147faeb-3de9-5026-a027-2d869da460b6',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name',
    display_name='Slakoth',
    searchable_by=['Slakoth', 'Basic', 'Slakoth'],
    subtypes=['Basic'],
    collector_number=168,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=287,
    abilities=[
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title='Boundless Power',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
