from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e5708535-1837-58da-9278-656e6a042aa6',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name',
    display_name='Onix',
    searchable_by=['Onix', 'Basic', 'Onix'],
    subtypes=['Basic'],
    collector_number=90,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=95,
    abilities=[
        Attack(
            title='Hard Headbutt',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Land Crush',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
