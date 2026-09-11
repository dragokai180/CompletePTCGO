from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0df1f45b-b18f-583c-b705-fbcbef259b32',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name',
    display_name='Phanpy',
    searchable_by=['Phanpy', 'Basic', 'Phanpy'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=231,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Endure',
            game_text="Flip a coin. If heads, if this Pokémon would be Knocked Out by damage from an attack during your opponent's next turn, it is not Knocked Out, and its remaining HP becomes 10.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
    ],
)
