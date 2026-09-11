from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bfbd5624-88e4-5cd7-b7d1-1bec5fb640c4',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name',
    display_name='Aron',
    searchable_by=['Aron', 'Basic', 'Aron'],
    subtypes=['Basic'],
    collector_number=42,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=304,
    abilities=[
        Attack(
            title='Metal Sound',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Confused.',
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
