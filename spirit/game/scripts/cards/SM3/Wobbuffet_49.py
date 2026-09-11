from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b00946fa-308f-5c71-8f17-337ebd9be754',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name',
    display_name='Wobbuffet',
    searchable_by=['Wobbuffet', 'Basic', 'Wobbuffet'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=202,
    abilities=[
        Attack(
            title='Shadowy Knot',
            game_text="This attack does 50 damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
