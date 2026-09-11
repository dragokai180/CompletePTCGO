from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2242642f-ee36-5e33-87ee-0521ad74e33f',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name',
    display_name='Koffing',
    searchable_by=['Koffing', 'Basic', 'Koffing'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=109,
    abilities=[
        Attack(
            title='Foul Gas',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned. If tails, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
