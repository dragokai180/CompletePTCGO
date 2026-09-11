from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dd79648f-5e1a-55cb-bb61-9b10218d6cb4',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name',
    display_name='Hoothoot',
    searchable_by=['Hoothoot', 'Basic', 'Hoothoot'],
    subtypes=['Basic'],
    collector_number=66,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
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
            title='Hypnosis',
            game_text='The Defending Pokémon is now Asleep.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
