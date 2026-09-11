from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4d5f420-50f9-5582-9b67-95160acbe3a2',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name',
    display_name='Latias',
    searchable_by=['Latias', 'Basic', 'Latias'],
    subtypes=['Basic'],
    collector_number=139,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=380,
    abilities=[
        Ability(
            title='Mist Float',
            game_text='If this Pokémon has any Psychic Energy attached, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has any Psychic Energy attached, it has no Retreat Cost.'),
        ),
        Attack(
            title='Psychic Sphere',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
