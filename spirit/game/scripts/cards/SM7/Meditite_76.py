from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6c6c1182-5748-5677-8cea-6333d9c4b13e',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name',
    display_name='Meditite',
    searchable_by=['Meditite', 'Basic', 'Meditite'],
    subtypes=['Basic'],
    collector_number=76,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=307,
    abilities=[
        Attack(
            title='Bide',
            game_text="Flip a coin. If heads, if this Pokémon would be Knocked Out by damage from an attack during your opponent's next turn, it is not Knocked Out, and its remaining HP becomes 10.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Kick',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)
