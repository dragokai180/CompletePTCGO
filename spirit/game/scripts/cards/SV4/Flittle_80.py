from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ca55ad92-5cb0-5364-b708-1b131b80066c',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name',
    display_name='Flittle',
    searchable_by=['Flittle', 'Basic', 'Flittle'],
    subtypes=['Basic'],
    collector_number=80,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=955,
    abilities=[
        Attack(
            title='Psychic',
            game_text="This attack does 10 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
