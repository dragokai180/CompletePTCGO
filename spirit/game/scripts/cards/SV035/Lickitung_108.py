from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='811e4690-29da-5ec8-98b2-ecd268bb0583',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name',
    display_name='Lickitung',
    searchable_by=['Lickitung', 'Basic', 'Lickitung'],
    subtypes=['Basic'],
    collector_number=108,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=108,
    abilities=[
        Attack(
            title='Tongue-Tied',
            game_text="During your opponent's next turn, the Defending Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
