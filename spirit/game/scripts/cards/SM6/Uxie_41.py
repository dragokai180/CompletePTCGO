from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='20cf65c6-5492-5e6c-8d7d-e2a448e9ce21',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name',
    display_name='Uxie',
    searchable_by=['Uxie', 'Basic', 'Uxie'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=480,
    abilities=[
        Attack(
            title='Memory Skip',
            game_text="Choose 1 of your opponent's Active Pokémon's attacks. That Pokémon can't use that attack during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
