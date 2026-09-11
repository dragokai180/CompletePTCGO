from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ae82d588-9daa-5c09-a494-b15c787f473a',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name',
    display_name='Koffing',
    searchable_by=['Koffing', 'Basic', 'Koffing'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=109,
    abilities=[
        Attack(
            title='Smokescreen',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Suffocating Gas',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
