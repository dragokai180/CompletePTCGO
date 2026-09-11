from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8beba7e6-f582-5a8b-97d4-f3eb9afd702b',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name',
    display_name='Hoothoot',
    searchable_by=['Hoothoot', 'Basic', 'Hoothoot'],
    subtypes=['Basic'],
    collector_number=165,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=163,
    abilities=[
        Attack(
            title='Air Slash',
            game_text='Discard an Energy from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
